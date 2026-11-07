import unittest

from manual_knowledge.extraction import extract_html


class ExtractionTests(unittest.TestCase):
    def test_word_headings_table_and_exact_codes(self):
        raw = '''<html><head><title>chrome</title></head><body>
        <script>hidden()</script><nav>navigation</nav>
        <p class="WD_HBÜ2"><a name="section"></a>Ä section</p>
        <p class="WD_HBÜ4">Details</p>
        <table><tr><th>Code</th><th>Value</th></tr>
        <tr><td><p class="WD_HBTabellenüberschrift">PUT</p></td>
        <td>Put<br>0,05 &lt;Null&gt;</td></tr></table>
        <img src="image004.jpg" alt="Diagram">
        <p class="WD_HBÜ2">Next</p></body></html>'''.encode()
        result = extract_html(raw, 'ä/topic.htm')
        self.assertNotIn('hidden', result['text'])
        self.assertNotIn('chrome', result['text'])
        self.assertNotIn('navigation', result['text'])
        self.assertEqual(result['tables'][0]['rows'][1][1]['text'], 'Put 0,05 <Null>')
        self.assertEqual(result['tables'][0]['rows'][0][0]['header'], True)
        self.assertEqual(result['tables'][0]['rows'][1][0]['header'], True)
        self.assertEqual(result['blocks'][0]['line'], 3)
        self.assertEqual(result['blocks'][0]['class'], 'WD_HBÜ2')
        self.assertEqual(result['images'][0]['local_path'], 'ä/image004.jpg')
        self.assertEqual([h['text'] for h in result['images'][0]['heading_path']], ['Ä section', 'Details'])
        self.assertEqual(result['blocks'][-1]['heading_path'], [{'level': 2, 'text': 'Next', 'anchors': []}])
        self.assertEqual(result, extract_html(raw, 'ä/topic.htm'))

    def test_assets_are_not_fetchable_or_allowed_to_escape(self):
        raw = b'<img src="../../escape.jpg"><img src="https://example.com/a.jpg"><img src="../common/a.jpg#x">'
        paths = [i['local_path'] for i in extract_html(raw, 'folder/a.htm')['images']]
        self.assertEqual(paths, [None, None, 'common/a.jpg'])

    def test_strict_encoding_and_path(self):
        with self.assertRaises(UnicodeDecodeError):
            extract_html(b'\xff', 'a.htm')
        for path in ['../a.htm', '/a.htm', 'C:/a.htm', 'a\\b.htm', 'a/./b.htm']:
            with self.assertRaises(ValueError):
                extract_html(b'<p>x</p>', path)

    def test_nested_tables_and_spans(self):
        result = extract_html(b'<table><tr><td colspan="2">Outer<table><tr><td>Inner</td></tr></table>End</td></tr></table>', 'a.htm')
        self.assertEqual(len(result['tables']), 2)
        self.assertEqual(result['tables'][0]['rows'][0][0]['text'], 'Outer End')
        self.assertEqual(result['tables'][0]['rows'][0][0]['colspan'], '2')
        self.assertEqual(result['tables'][1]['rows'][0][0]['text'], 'Inner')


if __name__ == '__main__':
    unittest.main()
