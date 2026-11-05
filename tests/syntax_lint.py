"""Проверка details/summary вне примеров кода; CLI: python tests/syntax_lint.py FILE."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys

from markdown_it import MarkdownIt

errors = []  # Совместимость с первоначальным API тестов.


def _text(lines):
    if isinstance(lines, str):
        return lines
    if isinstance(lines, bytes):
        return lines.decode('utf-8')
    return '\n'.join(_text(line) for line in lines)


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.frames = []
        self.issues = []
        self.counts = Counter()

    def handle_starttag(self, tag, attrs):
        if tag not in {'details', 'summary'}:
            return
        self.counts[tag] += 1
        if tag == 'details':
            self.frames.append({'summary': False})
        elif not self.frames or not self.stack or self.stack[-1] != 'details':
            self.issues.append('summary должен находиться непосредственно внутри details')
        elif self.frames[-1]['summary']:
            self.issues.append('Повторный summary в одном details')
        else:
            self.frames[-1]['summary'] = True
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in {'details', 'summary'}:
            return
        self.counts['/' + tag] += 1
        if not self.stack or self.stack[-1] != tag:
            self.issues.append(f'Нарушен порядок закрытия {tag}')
            return
        self.stack.pop()
        if tag == 'details':
            frame = self.frames.pop()
            if not frame['summary']:
                self.issues.append('В details отсутствует summary')


def structure(lines):
    parser = Structure()
    for token in MarkdownIt('commonmark').parse(_text(lines)):
        if token.type == 'html_block':
            parser.feed(token.content)
        for child in token.children or []:
            if child.type == 'html_inline':
                parser.feed(child.content)
    if parser.stack:
        parser.issues.append('Незакрытые теги в конце файла: ' + ', '.join(parser.stack))
    return parser


def count_details(file_list):
    counts = structure(file_list).counts
    return counts['details'] == counts['/details']


def count_summary(file_list):
    counts = structure(file_list).counts
    return counts['summary'] == counts['/summary']


def check_details_tag(file_list):
    errors.extend(structure(file_list).issues)


def check_summary_tag(file_list):
    errors.extend(structure(file_list).issues)


def check_md_file(file_name):
    errors.clear()
    errors.extend(structure(Path(file_name).read_text(encoding='utf-8')).issues)


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'README.md'
    check_md_file(target)
    if errors:
        print(target + ': ' + '; '.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print('Markdown structure OK:', target)
