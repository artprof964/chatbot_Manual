import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from manual_knowledge import bundles
from manual_knowledge.bundles import BundleError, canonical, capture, digest, validate


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        self.source.mkdir()
        for branch in ("changes", "änderungen"):
            folder = self.source / branch
            folder.mkdir()
            (folder / "topic.htm").write_text('<p class="WD_HBÜ1">Example</p><p>PUT &lt;Null&gt;</p>', encoding="utf-8")
        self.output = self.base / "bundle"

    def build(self):
        return capture(self.source, self.output, "synthetic", quiescent=True)

    def rewrite_manifest(self, manifest):
        body = {k: v for k, v in manifest.items() if k != "revision"}
        manifest["revision"] = digest(canonical(body))
        (self.output / "manifest.json").write_bytes(canonical(manifest))

    def test_deterministic_capture_and_duplicate_occurrences(self):
        first = self.build()
        self.assertEqual(len(first["occurrences"]), 2)
        self.assertEqual(len(list((self.output / "blobs").iterdir())), 1)
        self.assertNotEqual(first["occurrences"][0]["id"], first["occurrences"][1]["id"])
        os.utime(self.source / "changes/topic.htm", (10, 10))
        second = capture(self.source, self.base / "again", "synthetic", quiescent=True)
        self.assertEqual(first, second)
        self.assertEqual(validate(self.output), first)

    def test_quiescent_confirmation_overlap_and_overwrite_rejected(self):
        with self.assertRaises(BundleError):
            capture(self.source, self.output, "synthetic")
        for path in (self.source, self.source / "inside", self.base):
            with self.assertRaises(BundleError):
                capture(self.source, path, "synthetic", quiescent=True)
        self.build()
        with self.assertRaises(BundleError):
            self.build()

    def test_source_changes_abort_without_final_bundle(self):
        original = bundles.extract_html
        calls = 0
        def mutate(data, path):
            nonlocal calls
            calls += 1
            if calls == 1:
                (self.source / path).write_bytes(b'<p>Changed</p>')
            return original(data, path)
        with patch.object(bundles, "extract_html", side_effect=mutate):
            with self.assertRaisesRegex(BundleError, "changed"):
                self.build()
        self.assertFalse(self.output.exists())
        self.assertFalse(list(self.base.glob('.capture-*')))

    def test_inventory_change_aborts(self):
        original = bundles.extract_html
        def add(data, path):
            (self.source / "new.txt").write_text('new', encoding='utf-8')
            return original(data, path)
        with patch.object(bundles, "extract_html", side_effect=add):
            with self.assertRaisesRegex(BundleError, "inventory changed"):
                self.build()
        self.assertFalse(self.output.exists())

    def test_invalid_utf8_aborts(self):
        (self.source / 'bad.htm').write_bytes(b'\xff')
        with self.assertRaises(UnicodeDecodeError):
            self.build()
        self.assertFalse(self.output.exists())

    def test_unreadable_subtree_is_not_a_complete_capture(self):
        hidden = self.source / 'hidden'
        hidden.mkdir()
        (hidden / 'important.txt').write_text('evidence', encoding='utf-8')
        original = os.scandir
        def denied(path):
            if Path(path) == hidden:
                raise PermissionError('synthetic unreadable subtree')
            return original(path)
        with patch.object(os, 'scandir', side_effect=denied):
            with self.assertRaisesRegex(BundleError, 'unreadable'):
                self.build()
        self.assertFalse(self.output.exists())

    def test_image_identity_missing_and_external_are_explicit(self):
        (self.source / 'images.htm').write_text('<img src="ok.jpg"><img src="missing.jpg"><img src="https://example.com/x.jpg">', encoding='utf-8')
        (self.source / 'ok.jpg').write_bytes(b'synthetic image placeholder')
        self.build()
        rows = [json.loads(x) for x in (self.output / 'records.jsonl').read_bytes().splitlines()]
        assets = next(r for r in rows if r['extraction']['source_path'] == 'images.htm')['image_assets']
        self.assertEqual([x['status'] for x in assets], ['resolved', 'missing', 'external-or-unsafe'])
        self.assertEqual(assets[0]['sha256'], digest(b'synthetic image placeholder'))
        self.assertTrue(all(x['visual_review'] == 'unreviewed' for x in assets))

    def test_corrupt_blob_and_records_rejected(self):
        manifest = self.build()
        blob = self.output / 'blobs' / manifest['occurrences'][0]['sha256']
        data = blob.read_bytes()
        blob.write_bytes(b'corrupt')
        with self.assertRaisesRegex(BundleError, 'Blob'):
            validate(self.output)
        blob.write_bytes(data)
        (self.output / 'records.jsonl').write_bytes(b'{}\n')
        with self.assertRaisesRegex(BundleError, 'Records digest'):
            validate(self.output)

    def test_rehashed_tampered_extraction_rejected(self):
        manifest = self.build()
        rows = [json.loads(x) for x in (self.output / 'records.jsonl').read_bytes().splitlines()]
        rows[0]['extraction']['text'] = 'Invented meaning'
        raw = b''.join(canonical(r) + b'\n' for r in rows)
        (self.output / 'records.jsonl').write_bytes(raw)
        manifest['records_sha256'] = digest(raw)
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(BundleError, 'Extraction provenance'):
            validate(self.output)

    def test_rehashed_unsafe_path_and_duplicate_rejected(self):
        manifest = self.build()
        manifest['occurrences'][0]['path'] = '../escape'
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(BundleError, 'Unsafe'):
            validate(self.output)
        manifest['occurrences'][0] = manifest['occurrences'][1].copy()
        self.rewrite_manifest(manifest)
        with self.assertRaisesRegex(BundleError, 'Duplicate'):
            validate(self.output)

    def test_nested_link_rejected(self):
        try:
            (self.source / 'linked').symlink_to(self.base, target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks is not permitted on this host')
        with self.assertRaisesRegex(BundleError, 'Nested link'):
            self.build()


if __name__ == '__main__':
    unittest.main()
