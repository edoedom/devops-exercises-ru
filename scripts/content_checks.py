"""Проверка локальных Markdown-ссылок и якорей. Сеть не используется."""
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
PARSER = MarkdownIt("commonmark")
LEGACY_TRANSLATIONS = {"README-pt-BR.md", "README-zh_CN.md"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = set()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.anchors.add(attrs["name"])
        key = "href" if tag == "a" else "src" if tag == "img" else None
        if key and attrs.get(key):
            self.targets.append(attrs[key])


class Answers(HTMLParser):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.empty = []

    def handle_starttag(self, tag, attrs):
        if tag == 'details':
            self.frames.append({'summary': False, 'question': '', 'answer': ''})
        elif tag == 'summary' and self.frames:
            self.frames[-1]['summary'] = True

    def handle_data(self, data):
        if self.frames:
            key = 'question' if self.frames[-1]['summary'] else 'answer'
            self.frames[-1][key] += data

    def handle_endtag(self, tag):
        if tag == 'summary' and self.frames:
            self.frames[-1]['summary'] = False
        elif tag == 'details' and self.frames:
            frame = self.frames.pop()
            if not frame['question'].strip() or not frame['answer'].strip():
                self.empty.append(frame['question'].strip() or '(пустой вопрос)')


def unanswered(text):
    parser = Answers()
    parser.feed(PARSER.render(text))
    return parser.empty


def slug(text):
    text = unescape(text).lower()
    return "".join(c for c in text if c.isalnum() or c in "_- ").replace(" ", "-")


def parse_markdown(text):
    anchors, targets = set(), []
    duplicates = Counter()
    html = Links()
    tokens = PARSER.parse(text)
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            inline = tokens[i + 1]
            title = "".join(t.content for t in inline.children or []
                            if t.type in {"text", "code_inline", "image"})
            base = slug(title)
            suffix = f"-{duplicates[base]}" if duplicates[base] else ""
            anchors.add(base + suffix)
            duplicates[base] += 1
        if token.type == "html_block":
            html.feed(token.content)
        for child in token.children or []:
            if child.type == "link_open":
                targets.append(child.attrGet("href"))
            elif child.type == "image":
                targets.append(child.attrGet("src"))
            elif child.type == "html_inline":
                html.feed(child.content)
    anchors.update(html.anchors)
    targets.extend(html.targets)
    return anchors, targets


def paths(root):
    for p in sorted(root.rglob("*.md")):
        relative = p.relative_to(root)
        if (p.name in LEGACY_TRANSLATIONS or relative.parts[0] == "tests" or
                any(part.startswith(".") or part in {"node_modules", "venv", "__pycache__"}
                    for part in relative.parts)):
            continue
        yield p


def check_links(root):
    root = root.resolve()
    documents = {p.resolve(): parse_markdown(p.read_text(encoding="utf-8")) for p in paths(root)}
    cache = dict(documents)
    issues = []
    checked = 0
    for p, (_, targets) in documents.items():
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or target.startswith("//"):
                continue
            checked += 1
            dest = (p.parent / unquote(url.path)).resolve() if url.path else p
            if dest != root and root not in dest.parents:
                issues.append((str(p.relative_to(root)), target, "путь вне репозитория"))
            elif not dest.exists():
                issues.append((str(p.relative_to(root)), target, "файл отсутствует"))
            elif url.fragment and dest.suffix == ".md":
                if dest not in cache:
                    cache[dest] = parse_markdown(dest.read_text(encoding="utf-8"))
                if unquote(url.fragment) not in cache[dest][0]:
                    issues.append((str(p.relative_to(root)), target, "якорь отсутствует"))
    return checked, issues


def main():
    count, issues = check_links(ROOT)
    empty = [(str(p.relative_to(ROOT)), q) for p in paths(ROOT)
             if '-pt-BR' not in p.name
             for q in unanswered(p.read_text(encoding='utf-8'))]
    for p, target, reason in issues:
        print(f"{p}: {target}: {reason}", file=sys.stderr)
    print(f"Local references: {count}; errors: {len(issues)}")
    for p, question in empty:
        print(f'{p}: пустой вопрос/ответ: {question}', file=sys.stderr)
    print(f'Unanswered questions: {len(empty)}')
    if issues or empty:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
