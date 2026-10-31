"""Extract local public filing text; preserve rows for source verification."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'ix:header'):
            self.skip += 1
        if tag in ('p', 'div', 'tr', 'table', 'br'):
            self.parts.append('\n')
        if tag in ('td', 'th'):
            self.parts.append(' | ')
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'ix:header'):
            self.skip = max(0, self.skip - 1)
        if tag in ('p', 'div', 'tr'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

for arg in sys.argv[1:]:
    source = Path(arg)
    parser = Extractor()
    parser.feed(source.read_text())
    source.with_suffix('.txt').write_text(re.sub(r'\n\s*\n+', '\n', ''.join(parser.parts)))
