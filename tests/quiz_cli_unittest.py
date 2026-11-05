from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).resolve().parent.parent / 'scripts/random_question.py'


class QuizCLI(unittest.TestCase):
    def run_quiz(self, *args):
        with TemporaryDirectory() as tmp:
            return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=tmp,
                                  text=True, capture_output=True, timeout=15)

    def test_topic_list_from_any_working_directory(self):
        result = self.run_quiz('--list-topics')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('gitops', result.stdout.splitlines())
        self.assertIn('sre', result.stdout.splitlines())

    def test_seeded_question_and_answer_do_not_require_stdin(self):
        args = ('--topic', 'gitops', '--once', '--show-answer', '--seed', '42')
        first, second = self.run_quiz(*args), self.run_quiz(*args)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('Ответ:', first.stdout)
        self.assertNotIn('<summary>', first.stdout)
        self.assertNotIn('<b>', first.stdout)

    def test_unknown_topic_is_a_clear_error(self):
        result = self.run_quiz('--topic', 'does-not-exist', '--once')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Неизвестная тема', result.stderr)
