"""Check local evidence fingerprints without copying or modifying the manual."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', type=Path, default=Path(__file__).with_name('source_evidence.json'))
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1] / 'root_manual' / 'Handbuch' / 'de')
    args = parser.parse_args()
    registry = json.loads(args.registry.read_text(encoding='utf-8'))
    failures = []
    root = args.source.resolve(strict=True)
    for evidence_id, evidence in registry['evidence'].items():
        try:
            path = (root / evidence['path']).resolve(strict=True)
            if not path.is_relative_to(root):
                raise ValueError('Evidence path escapes source root')
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != evidence['sha256']:
                failures.append(evidence_id + ': fingerprint mismatch')
        except (OSError, ValueError) as error:
            failures.append(evidence_id + ': ' + str(error))
    print(json.dumps({'checked': len(registry['evidence']), 'failures': failures}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
