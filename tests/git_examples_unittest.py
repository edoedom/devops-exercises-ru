import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GitExamplesTest(unittest.TestCase):
    def run_example(self, document, repo_name):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        editor = directory / 'sequence.sh'
        editor.write_text('#!/bin/sh\nsed "2s/^pick /squash /" "$1" > "$1.tmp" && mv "$1.tmp" "$1"\n')
        editor.chmod(0o700)
        env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
                   GIT_SEQUENCE_EDITOR=str(editor), GIT_EDITOR='true',
                   GIT_TERMINAL_PROMPT='0')
        content = (ROOT / 'topics/git/solutions' / document).read_text()
        blocks = re.findall(r'```bash\n(.*?)```', content, re.S)
        self.assertTrue(blocks)
        result = subprocess.run(['bash', '-eu', '-c', '\n'.join(blocks)],
                                cwd=directory, env=env, text=True,
                                capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        repo = directory / repo_name

        def git(*args):
            return subprocess.check_output(['git', *args], cwd=repo,
                                           env=env, text=True).strip()
        self.assertEqual(git('status', '--porcelain'), '')
        return git, result.stdout

    def test_first_commit(self):
        git, _ = self.run_example('commit_01_solution.md', 'my_repo')
        self.assertEqual(git('show', 'HEAD:file'), 'hello commit')
        self.assertEqual(git('rev-list', '--count', 'HEAD'), '1')

    def test_branch_isolation(self):
        git, _ = self.run_example('branch_01_solution.md', 'branch_lab')
        self.assertEqual(git('rev-list', '--count', 'main..dev'), '1')
        self.assertEqual(git('rev-list', '--count', 'dev..main'), '0')
        self.assertEqual(git('show', 'main:file'), 'main version')
        self.assertEqual(git('show', 'dev:file'), 'dev version')
        self.assertEqual(git('branch', '--show-current'), 'main')

    def test_root_squash_preserves_tree(self):
        git, output = self.run_example('squashing_commits.md', 'squash_lab')
        self.assertEqual(git('rev-list', '--count', 'HEAD'), '1')
        self.assertEqual(git('show', 'HEAD:new_file'), 'Mario & Luigi')
        trees = re.findall(r'^[0-9a-f]{40,64}$', output, re.M)
        self.assertEqual(len(trees), 2)
        self.assertEqual(trees[0], trees[1])


if __name__ == '__main__':
    unittest.main()
