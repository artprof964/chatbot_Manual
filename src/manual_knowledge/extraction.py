"""Deterministic, non-executing extraction of RoboHelp evidence.

This is a structural baseline, not a browser or an OCR engine. Only explicit
head/script/style/nav/footer chrome is discarded; unknown chrome is retained.
"""

from html.parser import HTMLParser
import posixpath
import re
from urllib.parse import unquote, urlsplit


def _text(parts):
    return " ".join("".join(parts).split())


class _Extractor(HTMLParser):
    def __init__(self, source_path, has_body):
        super().__init__(convert_charrefs=True)
        self.source_path = source_path
        self.in_body = not has_body
        self.skip = []
        self.blocks = []
        self.tables = []
        self.images = []
        self.anchors = []
        self.headings = []
        self.paragraph = None
        self.table_stack = []
        self.all_text = []
        self.warnings = []

    def _path(self):
        return [dict(h) for h in self.headings]

    def _finish_paragraph(self):
        if self.paragraph is None:
            return
        block = self.paragraph
        self.paragraph = None
        block['text'] = _text(block.pop('parts'))
        level = block.get('level')
        if level is not None and block['text']:
            self.headings = [h for h in self.headings if h['level'] < level]
            self.headings.append({'level': level, 'text': block['text'],
                                  'anchors': list(block['anchors'])})
        block['heading_path'] = self._path()
        if block['text'] or block['anchors']:
            self.blocks.append(block)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'body':
            self.in_body = True
        if self.skip:
            if tag in {'head', 'script', 'style', 'nav', 'footer'}:
                self.skip.append(tag)
            return
        if tag in {'head', 'script', 'style', 'nav', 'footer'}:
            self.skip.append(tag)
            return
        if not self.in_body:
            return
        if tag in {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self._finish_paragraph()
            match = re.search(r'(?:^|\s)WD_HBÜ([1-6])(?:\s|$)', attrs.get('class', ''))
            level = int(tag[1]) if tag.startswith('h') else int(match[1]) if match else None
            self.paragraph = {'kind': 'heading' if level else 'paragraph',
                              'parts': [], 'anchors': [], 'line': self.getpos()[0],
                              'class': attrs.get('class', '')}
            if level:
                self.paragraph['level'] = level
            if ('WD_HBTabellenüberschrift' in attrs.get('class', '').split()
                    and self.table_stack and self.table_stack[-1]['cell'] is not None):
                self.table_stack[-1]['cell']['header'] = True
        for anchor in dict.fromkeys([attrs.get('id'), attrs.get('name') if tag == 'a' else None]):
            if anchor:
                self.anchors.append({'anchor': anchor, 'line': self.getpos()[0]})
                if self.paragraph is not None:
                    self.paragraph['anchors'].append(anchor)
        if tag == 'table':
            table = {'rows': [], 'heading_path': self._path(), 'line': self.getpos()[0]}
            self.tables.append(table)
            self.table_stack.append({'table': table, 'row': None, 'cell': None})
        elif tag == 'tr' and self.table_stack:
            state = self.table_stack[-1]
            state['row'] = []
            state['cell'] = None
            state['table']['rows'].append(state['row'])
        elif tag in {'td', 'th'} and self.table_stack:
            state = self.table_stack[-1]
            if state['row'] is None:
                state['row'] = []
                state['table']['rows'].append(state['row'])
            cell = {'text': '', 'header': tag == 'th', 'rowspan': attrs.get('rowspan', '1'),
                    'colspan': attrs.get('colspan', '1'), '_parts': []}
            state['row'].append(cell)
            state['cell'] = cell
        elif tag == 'img':
            src = attrs.get('src', '')
            parsed = urlsplit(src)
            decoded = unquote(parsed.path).replace('\\', '/')
            candidate = posixpath.normpath(posixpath.join(posixpath.dirname(self.source_path), decoded))
            safe = (bool(decoded) and not parsed.scheme and not parsed.netloc
                    and not decoded.startswith('/') and ':' not in decoded
                    and candidate != '..' and not candidate.startswith('../'))
            self.images.append({'src': src, 'local_path': candidate if safe else None,
                                'alt': attrs.get('alt', ''), 'heading_path': self._path(),
                                'line': self.getpos()[0]})
        if tag in {'br', 'p', 'tr', 'td', 'th', 'div', 'li'}:
            self.handle_data(' ')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if self.skip:
            if tag == self.skip[-1]:
                self.skip.pop()
            return
        if not self.in_body:
            return
        if tag in {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.handle_data(' ')
            self._finish_paragraph()
        if tag in {'td', 'th'} and self.table_stack:
            self.table_stack[-1]['cell'] = None
        elif tag == 'table' and self.table_stack:
            self.table_stack.pop()
        if tag in {'div', 'li', 'tr', 'table'}:
            self.handle_data(' ')
        if tag == 'body':
            self.in_body = False

    def handle_data(self, data):
        if self.skip or not self.in_body:
            return
        self.all_text.append(data)
        if self.paragraph is not None:
            self.paragraph['parts'].append(data)
        # Nested table text belongs to its own cell, not the parent's cell.
        if self.table_stack and self.table_stack[-1]['cell'] is not None:
            self.table_stack[-1]['cell']['_parts'].append(data)

    def result(self):
        self._finish_paragraph()
        for table in self.tables:
            for row in table['rows']:
                for cell in row:
                    cell['text'] = _text(cell.pop('_parts'))
        if self.skip or self.table_stack:
            self.warnings.append('Unclosed structural element; inspect source before using as an oracle.')
        return {'schema_version': 1, 'source_path': self.source_path,
                'text': _text(self.all_text), 'blocks': self.blocks,
                'tables': self.tables, 'images': self.images,
                'anchors': self.anchors, 'warnings': self.warnings}


def extract_html(data: bytes, source_path: str) -> dict:
    """Extract UTF-8 bytes without fetching assets or executing active content.

    source_path is a POSIX relative corpus path, preserving Unicode and case.
    Span values are retained, not expanded; CSS layout/visibility is not modeled.
    """
    if (not source_path or '\\' in source_path or source_path.startswith('/')
            or ':' in source_path or any(p in {'', '.', '..'} for p in source_path.split('/'))):
        raise ValueError('source_path must be a normalized relative POSIX path')
    source = data.decode('utf-8-sig', errors='strict')
    parser = _Extractor(source_path, bool(re.search(r'<body\b', source, re.I)))
    parser.feed(source)
    parser.close()
    return parser.result()
