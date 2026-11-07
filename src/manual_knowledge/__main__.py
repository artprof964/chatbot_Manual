import argparse
import json
from pathlib import Path
from .bundles import BundleError, capture, validate


def main():
    parser = argparse.ArgumentParser(description="Local immutable manual evidence bundles")
    subs = parser.add_subparsers(dest="command", required=True)
    cap = subs.add_parser("capture")
    cap.add_argument("source", type=Path)
    cap.add_argument("output", type=Path)
    cap.add_argument("--dataset", required=True)
    cap.add_argument("--quiescent-source", action="store_true", help="Confirm source is a quiescent export or snapshot")
    val = subs.add_parser("validate")
    val.add_argument("bundle", type=Path)
    args = parser.parse_args()
    try:
        result = capture(args.source, args.output, args.dataset, quiescent=args.quiescent_source) if args.command == "capture" else validate(args.bundle)
    except (BundleError, OSError, UnicodeError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    print(json.dumps({"revision": result["revision"], "occurrences": len(result["occurrences"]), "records": result["record_count"]}))


if __name__ == "__main__":
    main()
