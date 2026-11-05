from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.content_checks import check_links, parse_markdown


class ContentChecks(unittest.TestCase):
    def test_unicode_anchors_duplicate_headings_and_html(self):
        anchors, targets = parse_markdown('# Ёж и сеть\n\n# Ёж и сеть\n<a id="keep-id"></a>\n'
                                          '<img src="image.png">\n[Раздел](#ёж-и-сеть-1)')
        self.assertTrue({'ёж-и-сеть', 'ёж-и-сеть-1', 'keep-id'} <= anchors)
        self.assertIn('image.png', targets)

    def test_escaped_and_code_examples_are_not_links(self):
        _, links = parse_markdown('```md\n[пример](missing.md)\n```\n\n'
                                  '`[пример](another.md)`\n\\<a href="fake.md">')
        self.assertEqual(links, [])

    def test_balanced_parentheses_and_reference_links(self):
        _, links = parse_markdown('[wiki](https://example.org/Title_(extra))\n\n[x][ref]\n'
                                  '\n[ref]: folder/file.md#one')
        self.assertIn('https://example.org/Title_(extra)', links)
        self.assertIn('folder/file.md#one', links)

    def test_missing_anchor_file_and_escape(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('[A](ok.md#right) [B](ok.md#wrong) '
                                           '[C](gone.md) [D](../outside.md)', encoding='utf-8')
            (root / 'ok.md').write_text('<a id="right"></a>', encoding='utf-8')
            checked, issues = check_links(root)
        self.assertEqual(checked, 4)
        self.assertEqual({reason for _, _, reason in issues},
                         {'якорь отсутствует', 'файл отсутствует', 'путь вне репозитория'})

    def test_encoded_spaces_and_legacy_target(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'a b.md').write_text('# Заголовок', encoding='utf-8')
            (root / 'README-pt-BR.md').write_text('# Intro', encoding='utf-8')
            (root / 'README.md').write_text('[A](a%20b.md#заголовок) '
                                           '[B](README-pt-BR.md#intro)', encoding='utf-8')
            _, issues = check_links(root)
        self.assertEqual(issues, [])

class QuestionMarkup(unittest.TestCase):
    def test_unclosed_tags_and_summary_outside_details(self):
        from tests.syntax_lint import structure
        self.assertTrue(structure('<details><summary>Q</summary>').issues)
        self.assertTrue(structure('<summary>Q</summary>').issues)
        self.assertTrue(structure('<details>No summary</details>').issues)

    def test_wrong_order_and_repeated_summary(self):
        from tests.syntax_lint import structure
        self.assertTrue(structure('<details><summary>Q</details></summary>').issues)
        self.assertTrue(structure('<details><summary>A</summary><summary>B</summary></details>').issues)

    def test_fenced_example_and_comment_are_not_live_markup(self):
        from tests.syntax_lint import structure
        self.assertFalse(structure('```html\n<details><summary>example\n```\n\n'
                                   '<!-- <summary>ignored -->').issues)
        self.assertFalse(structure('<details>\n<summary>Q</summary>\n\nAnswer\n</details>').issues)

class AnswerQuality(unittest.TestCase):
    def test_comment_and_empty_formatting_are_not_an_answer(self):
        from scripts.content_checks import unanswered
        self.assertEqual(unanswered('<details><summary>Q</summary>\n\n<!-- later -->\n</details>'), ['Q'])

    def test_code_is_an_answer_but_code_templates_are_not_questions(self):
        from scripts.content_checks import unanswered
        text = '<details>\n<summary>Q</summary>\n\n```py\nprint(1)\n```\n\n</details>'
        self.assertEqual(unanswered(text), [])
        self.assertEqual(unanswered('```html\n<details><summary>Example</summary></details>\n```'), [])

    def test_image_alone_needs_a_text_explanation(self):
        from scripts.content_checks import unanswered
        self.assertEqual(unanswered('<details><summary>Q</summary><img src="a.png"></details>'), ['Q'])
