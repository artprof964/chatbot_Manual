"""Version-one local bundles. Capture requires an externally quiescent source."""
from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import tempfile
from pathlib import Path, PurePosixPath

from .extraction import extract_html


class BundleError(ValueError):
    pass


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def _linked(path):
    attrs = getattr(path.lstat(), "st_file_attributes", 0)
    return path.is_symlink() or bool(attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def _inventory(root):
    result = []
    def fail(error):
        raise BundleError(f"Source inventory is unreadable: {error}") from error
    for current, dirs, files in os.walk(root, followlinks=False, onerror=fail):
        base = Path(current)
        for name in dirs + files:
            if _linked(base / name):
                raise BundleError(f"Nested link is not allowed: {base / name}")
        for name in files:
            p = base / name
            if not p.is_file():
                raise BundleError(f"Not a regular file: {p}")
            result.append(p.relative_to(root).as_posix())
    return sorted(result)


def _record(data, occurrence, by_path):
    extraction = extract_html(data, occurrence["path"])
    assets = []
    for image in extraction["images"]:
        path = image["local_path"]
        target = by_path.get(path)
        assets.append({"src": image["src"], "path": path,
                       "status": "resolved" if target else "missing" if path else "external-or-unsafe",
                       "occurrence_id": target["id"] if target else None,
                       "sha256": target["sha256"] if target else None,
                       "visual_review": "unreviewed"})
    return {"occurrence_id": occurrence["id"], "source_sha256": occurrence["sha256"],
            "extraction": extraction, "image_assets": assets}


def _path(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value or "\x00" in value:
        raise BundleError("Invalid relative path")
    p = PurePosixPath(value)
    if p.is_absolute() or any(x in ("", ".", "..") for x in value.split("/")):
        raise BundleError("Unsafe relative path")
    return value


def _hash(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
        raise BundleError("Invalid SHA-256")
    return value


def capture(source: Path, output: Path, dataset: str, *, quiescent=False):
    """Create a new bundle directory atomically; never write beneath source."""
    source, output = Path(source).resolve(), Path(output).resolve()
    if not quiescent:
        raise BundleError("A quiescent export or read-only snapshot is required")
    if not isinstance(dataset, str) or not dataset.strip():
        raise BundleError("Dataset must be nonempty")
    if not source.is_dir():
        raise BundleError("Source directory is unavailable")
    if output == source or source in output.parents or output in source.parents:
        raise BundleError("Source and output must not overlap")
    if output.exists():
        raise BundleError("Output must be a new directory")
    paths = _inventory(source)
    if not paths:
        raise BundleError("Empty source is not accepted as a complete snapshot")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".capture-", dir=output.parent) as stage_name:
        stage = Path(stage_name)
        (stage / "blobs").mkdir()
        occurrences, records = [], []
        for name in paths:
            _path(name)
            data = (source / name).read_bytes()
            sha = digest(data)
            blob = stage / "blobs" / sha
            if not blob.exists():
                blob.write_bytes(data)
            occurrence = {"path": name, "sha256": sha, "size": len(data),
                          "id": digest(canonical([dataset, name]))}
            occurrences.append(occurrence)
        by_path = {item["path"]: item for item in occurrences}
        for occurrence in occurrences:
            if Path(occurrence["path"]).suffix.lower() in (".htm", ".html"):
                records.append(_record((stage / "blobs" / occurrence["sha256"]).read_bytes(), occurrence, by_path))
        if paths != _inventory(source):
            raise BundleError("Source inventory changed during capture")
        for occurrence in occurrences:
            if digest((source / occurrence["path"]).read_bytes()) != occurrence["sha256"]:
                raise BundleError("Source bytes changed during capture")
        record_bytes = b"".join(canonical(r) + b"\n" for r in records)
        (stage / "records.jsonl").write_bytes(record_bytes)
        body = {"schema_version": 1, "dataset": dataset, "capture_policy": "quiescent-source",
                "extractor_version": "1", "occurrences": occurrences,
                "records_sha256": digest(record_bytes), "record_count": len(records)}
        manifest = {**body, "revision": digest(canonical(body))}
        (stage / "manifest.json").write_bytes(canonical(manifest) + b"\n")
        validate(stage)
        # Move the staged directory, then recreate it for TemporaryDirectory cleanup.
        os.rename(stage, output)
        stage.mkdir()
    return manifest


def validate(bundle: Path):
    """Check structure, digests, occurrence identity and extracted record coverage."""
    root = Path(bundle).resolve()
    try:
        _inventory(root)  # Reject nested links before reading referenced files.
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise BundleError("Manifest must be an object")
        expected = {"schema_version", "dataset", "capture_policy", "extractor_version", "occurrences", "records_sha256", "record_count", "revision"}
        if set(manifest) != expected or manifest["schema_version"] != 1:
            raise BundleError("Unsupported manifest schema")
        if manifest["capture_policy"] != "quiescent-source" or manifest["extractor_version"] != "1":
            raise BundleError("Unsupported capture/extractor policy")
        dataset = manifest["dataset"]
        if not isinstance(dataset, str) or not dataset.strip():
            raise BundleError("Invalid dataset")
        body = {k: v for k, v in manifest.items() if k != "revision"}
        if digest(canonical(body)) != _hash(manifest["revision"]):
            raise BundleError("Manifest digest mismatch")
        occurrences = manifest["occurrences"]
        if not isinstance(occurrences, list) or not occurrences:
            raise BundleError("Missing complete occurrence inventory")
        seen, ids, html = set(), set(), {}
        for item in occurrences:
            if not isinstance(item, dict) or set(item) != {"path", "sha256", "size", "id"}:
                raise BundleError("Invalid occurrence schema")
            name, sha = _path(item["path"]), _hash(item["sha256"])
            oid = digest(canonical([dataset, name]))
            if name in seen or oid in ids or item["id"] != oid:
                raise BundleError("Duplicate or invalid occurrence identity")
            seen.add(name)
            ids.add(oid)
            data = (root / "blobs" / sha).read_bytes()
            if type(item["size"]) is not int or item["size"] < 0 or len(data) != item["size"] or digest(data) != sha:
                raise BundleError("Blob length/digest mismatch")
            if Path(name).suffix.lower() in (".htm", ".html"):
                html[oid] = (sha, name, data)
        if [x["path"] for x in occurrences] != sorted(seen):
            raise BundleError("Inventory must be sorted")
        by_path = {item["path"]: item for item in occurrences}
        raw = (root / "records.jsonl").read_bytes()
        if digest(raw) != _hash(manifest["records_sha256"]):
            raise BundleError("Records digest mismatch")
        records = [json.loads(line) for line in raw.decode("utf-8").splitlines()]
        if type(manifest["record_count"]) is not int or len(records) != manifest["record_count"] or len(records) != len(html):
            raise BundleError("Record coverage mismatch")
        record_ids = set()
        for record in records:
            if not isinstance(record, dict) or set(record) != {"occurrence_id", "source_sha256", "extraction", "image_assets"}:
                raise BundleError("Invalid extraction record")
            oid = record["occurrence_id"]
            if oid in record_ids or oid not in html:
                raise BundleError("Duplicate or dangling record")
            record_ids.add(oid)
            sha, name, data = html[oid]
            if record != _record(data, by_path[name], by_path):
                raise BundleError("Extraction provenance/content mismatch")
        return manifest
    except (OSError, UnicodeError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise BundleError(f"Invalid or incomplete bundle: {exc}") from exc
