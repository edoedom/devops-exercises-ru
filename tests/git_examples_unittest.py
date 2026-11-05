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


class GitStateTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        self.env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_EDITOR='true', GIT_TERMINAL_PROMPT='0')
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write('base')
        self.git('add', 'file')
        self.git('commit', '-m', 'base')

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.repo,
                                       env=self.env, text=True, stderr=subprocess.PIPE).strip()

    def write(self, text):
        (self.repo / 'file').write_text(text + '\n')

    def test_diff_distinguishes_index_worktree_and_untracked(self):
        self.write('staged')
        self.git('add', 'file')
        self.write('working')
        (self.repo / 'untracked').write_text('new')
        self.assertIn('+staged', self.git('diff', '--cached'))
        self.assertIn('-staged', self.git('diff'))
        self.assertIn('+working', self.git('diff', 'HEAD'))
        self.assertEqual(self.git('diff', '--name-only', 'HEAD'), 'file')
        self.assertIn('?? untracked', self.git('status', '--short'))

    def test_restore_uses_index_by_default(self):
        self.write('staged')
        self.git('add', 'file')
        self.write('working')
        self.git('restore', '--worktree', '--', 'file')
        self.assertEqual((self.repo / 'file').read_text(), 'staged\n')
        self.git('restore', '--staged', '--', 'file')
        self.assertEqual(self.git('show', ':file'), 'base')
        self.assertEqual((self.repo / 'file').read_text(), 'staged\n')

    def check_reset(self, mode, index, working):
        base = self.git('rev-parse', 'HEAD')
        self.write('committed')
        self.git('add', 'file')
        self.git('commit', '-m', 'second')
        self.write('staged')
        self.git('add', 'file')
        self.write('working')
        self.git('reset', mode, 'HEAD~1')
        self.assertEqual(self.git('rev-parse', 'HEAD'), base)
        self.assertEqual(self.git('show', ':file'), index)
        self.assertEqual((self.repo / 'file').read_text(), working + '\n')

    def test_reset_soft(self):
        self.check_reset('--soft', 'staged', 'working')

    def test_reset_mixed(self):
        self.check_reset('--mixed', 'base', 'working')

    def test_reset_hard(self):
        self.check_reset('--hard', 'base', 'base')

    def test_fetch_does_not_integrate_and_ff_only_rejects_divergence(self):
        source = self.repo / 'source'
        self.git('clone', '--no-hardlinks', str(self.repo), str(source))
        def remote(*args):
            return subprocess.check_output(['git', '-C', str(source), *args],
                                           env=self.env, text=True, stderr=subprocess.PIPE).strip()
        remote('config', 'user.name', 'Test')
        remote('config', 'user.email', 'test@example.invalid')
        (source / 'remote-file').write_text('remote')
        remote('add', 'remote-file')
        remote('commit', '-m', 'remote change')
        self.git('remote', 'add', 'origin', str(source))
        self.write('local')
        self.git('add', 'file')
        self.git('commit', '-m', 'local change')
        before = self.git('rev-parse', 'HEAD')
        self.git('fetch', 'origin')
        self.assertEqual(self.git('rev-parse', 'HEAD'), before)
        self.assertEqual(self.git('rev-parse', 'origin/main'), remote('rev-parse', 'HEAD'))
        with self.assertRaises(subprocess.CalledProcessError):
            self.git('pull', '--ff-only', 'origin', 'main')
        self.assertEqual(self.git('rev-parse', 'HEAD'), before)
        self.assertFalse((self.repo / 'remote-file').exists())


if __name__ == '__main__':
    unittest.main()
