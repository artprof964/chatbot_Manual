"""Reproduce the bounded HTML inventory used by DATABASE_RESEARCH.md.

Run from the project root: python docs/research/profile_corpus.py
Reads the external source; writes only docs/research/CORPUS_PROFILE.json.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import statistics

BASE = Path("root_manual/Handbuch/de")
TREES = ["01-pms_online_handbuch", "02-pms_online_standardschnittstelle",
         "03-pms_aenderungsprotokolle", "03-pms_änderungsprotokolle"]


class Profile(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignored = 0
        self.parts = []
        self.headings = self.tables = self.links = self.images = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.ignored += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings += 1
        if tag == "table":
            self.tables += 1
        if tag == "a" and any(key == "href" for key, _ in attrs):
            self.links += 1
        if tag == "img":
            self.images += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.ignored:
            self.ignored -= 1

    def handle_data(self, data):
        if not self.ignored and data.strip():
            self.parts.append(data.strip())


def main():
    all_rows, summaries = [], []
    for tree in TREES:
        rows = []
        paths = list((BASE / tree).rglob("*.htm"))
        if not paths:
            raise RuntimeError(f"No source topics found: {BASE / tree}")
        for path in paths:
            parser = Profile()
            parser.feed(path.read_text(encoding="utf-8", errors="replace"))
            rows.append({"path": path.relative_to(BASE).as_posix(),
                         "text_chars": len(" ".join(parser.parts)),
                         "headings": parser.headings, "tables": parser.tables,
                         "links": parser.links, "image_refs": parser.images})
        summary = {"tree": tree, "pages": len(rows)}
        for key in ("text_chars", "headings", "tables", "links", "image_refs"):
            summary[key] = sum(row[key] for row in rows)
        summary["median_page_chars"] = int(statistics.median(row["text_chars"] for row in rows))
        summaries.append(summary)
        all_rows.extend(rows)
    result = {
        "method": "Python HTMLParser; UTF-8 replacement on errors; script/style data excluded; visible text approximate, not rendered, duplicate pages retained",
        "trees": summaries, "total_pages": len(all_rows),
        "largest_pages": sorted(all_rows, key=lambda row: row["text_chars"], reverse=True)[:8],
    }
    destination = Path("docs/research/CORPUS_PROFILE.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
