"""Black-box Bash exercises: temporary files and fake ping; no network access."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'topics/shell/solutions/scripts'
BASH = shutil.which('bash')


class ShellExercises(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cwd = Path(self.temp.name)

    def run_script(self, name, *args, input='', env=None):
        return subprocess.run([BASH, str(SCRIPTS / f'{name}.sh'), *map(str, args)],
                              cwd=self.cwd, input=input, text=True, capture_output=True,
                              timeout=10, env={**os.environ, 'LC_ALL': 'C.UTF-8', **(env or {})})

    def ok(self, name, *args, output, **kwargs):
        result = self.run_script(name, *args, **kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, output)
        self.assertEqual(result.stderr, '')

    def test_sum_decimal_sign_and_leading_zeroes(self):
        for left, right, expected in [('008', '010', 18), ('-008', '+010', 2),
                                      ('-0', '0', 0), ('999999999', '999999999', 1999999998)]:
            with self.subTest(left=left, right=right):
                self.ok('sum', left, right, output=f'{expected}\n')

    def test_sum_rejects_invalid_inputs_before_arithmetic(self):
        for value in ['', '1.5', '1+2', '1e3', '0x10', '1000000000', ' 1',
                      'x[$(touch INJECTED)]', '--1']:
            with self.subTest(value=value):
                result = self.run_script('sum', value, '2')
                self.assertEqual(result.returncode, 2)
                self.assertTrue(result.stderr)
                self.assertEqual(result.stdout, '')
        self.assertFalse((self.cwd / 'INJECTED').exists())

    def test_exact_argument_counts(self):
        cases = [('sum', []), ('sum', ['1']), ('sum', ['1', '2', '3']),
                 ('factors', []), ('factors', ['2', '3']), ('argument_check', []),
                 ('argument_check', ['a', 'b']), ('great_day', ['a', 'b']),
                 ('basic_date', ['x']), ('hello_world', ['x']), ('files_size', ['x']),
                 ('count_chars', ['x']), ('empty_files', []),
                 ('directories_comparison', ['one']), ('host_status', [])]
        for name, args in cases:
            with self.subTest(name=name, args=args):
                self.assertEqual(self.run_script(name, *args).returncode, 2)

    def test_factors_priority_and_negative_values(self):
        for number, expected in [('6', 'one factor...actually two!'), ('3', 'one factor...actually two!'),
                                 ('0', 'one factor...actually two!'), ('-004', 'one factor'), ('+005', '5')]:
            self.ok('factors', number, output=expected + '\n')
        self.assertEqual(self.run_script('factors', '1.5').returncode, 2)

    def test_argument_check_exact_string(self):
        self.ok('argument_check', 'pizza', output='with pineapple?\n')
        for value in ['', 'Pizza', 'pizza pie', '*']:
            self.ok('argument_check', value, output='I want pizza!\n')

    def test_great_day_distinguishes_missing_and_empty(self):
        self.ok('great_day', output='Today is a great day!\n')
        self.ok('great_day', '', output='Today is \n')
        self.ok('great_day', 'a sunny day', output='Today is a sunny day\n')

    def test_num_of_args_all_branches(self):
        self.assertEqual(self.run_script('num_of_args').returncode, 2)
        self.ok('num_of_args', '', output='Got it: \n')
        result = self.run_script('num_of_args', 'a', 'b')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr, 'hey hey...too many!\n')

    def test_print_arguments_preserves_boundaries(self):
        self.ok('print_arguments', 'two words', '', '*',
                output='First: two words\nCount: 3\nArg: two words\nArg: \nArg: *\n')
        self.ok('print_arguments', output='First: \nCount: 0\n')

    def test_hello_world_overwrites_file(self):
        target = self.cwd / 'amazing_output.txt'
        target.write_text('old content longer than new')
        self.ok('hello_world', output='')
        self.assertEqual(target.read_text(), 'Hello World\n')

    def test_date_format_and_failure(self):
        binary = self.cwd / 'date'
        binary.write_text('#!/bin/sh\n[ "$1" = +%F ] || exit 9\nprintf "2026-11-05\\n"\n')
        binary.chmod(0o755)
        self.ok('basic_date', output='', env={'PATH': str(self.cwd)})
        self.assertEqual((self.cwd / 'the_date.txt').read_text(), '2026-11-05\n')
        binary.write_text('#!/bin/sh\nexit 9\n')
        self.assertEqual(self.run_script('basic_date', env={'PATH': str(self.cwd)}).returncode, 9)

    def test_count_chars_preserves_whitespace_and_backslashes(self):
        self.ok('count_chars', input='  a\\b  \nlast', output='7\n4\n')

    def test_count_chars_unicode_codepoints(self):
        self.ok('count_chars', input='Привет\n😀\nе\u0301\n', output='6\n1\n2\n')

    def test_count_chars_stops_on_empty_line_and_handles_eof(self):
        self.ok('count_chars', input='one\n\nignored\n', output='3\n')
        self.ok('count_chars', input='', output='')
        self.ok('count_chars', input='\n', output='')

    def directories(self):
        left, right = self.cwd / '-first dir', self.cwd / 'second\ndir'
        left.mkdir(); right.mkdir()
        return left, right

    def test_compare_detects_contents_not_only_names(self):
        left, right = self.directories()
        (left / 'same name').write_text('one')
        (right / 'same name').write_text('two')
        result = self.run_script('directories_comparison', left, right)
        self.assertEqual(result.returncode, 1)
        self.assertTrue(result.stdout)
        (right / 'same name').write_text('one')
        self.ok('directories_comparison', left, right, output='')

    def test_compare_hidden_nested_and_literal_symlinks(self):
        left, right = self.directories()
        for directory in [left, right]:
            (directory / '.hidden').mkdir()
            (directory / '.hidden' / 'line\nbreak').write_text('same')
            (directory / 'link').symlink_to('missing target')
        self.ok('directories_comparison', left, right, output='')
        (right / 'link').unlink()
        (right / 'link').symlink_to('different missing target')
        self.assertEqual(self.run_script('directories_comparison', left, right).returncode, 1)
        (right / 'link').unlink()
        (right / 'link').symlink_to('missing target')
        (right / '.hidden' / 'line\nbreak').write_text('changed')
        self.assertEqual(self.run_script('directories_comparison', left, right).returncode, 1)

    def test_compare_missing_directory_is_error(self):
        self.assertEqual(self.run_script('directories_comparison', self.cwd, 'missing').returncode, 2)

    def empty_tree(self):
        target = self.cwd / '-directory\n'
        target.mkdir()
        (target / '.nested').mkdir()
        empty = [target / 'zero file', target / '.nested' / '-line\nbreak']
        for path in empty:
            path.touch()
        (target / 'keep').write_text('content')
        outside = self.cwd / 'outside'; outside.mkdir()
        (outside / 'empty').touch()
        (target / 'external').symlink_to(outside, target_is_directory=True)
        (target / 'symlink').symlink_to(empty[0])
        return target, empty, outside

    def test_empty_preview_is_non_destructive(self):
        target, empty, _ = self.empty_tree()
        result = self.run_script('empty_files', target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.splitlines()), 2)
        self.assertTrue(all(path.exists() for path in empty))

    def test_empty_apply_only_deletes_empty_regular_files(self):
        target, empty, outside = self.empty_tree()
        result = self.run_script('empty_files', '--apply', target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.splitlines()), 2)
        self.assertTrue(all(not path.exists() for path in empty))
        self.assertEqual((target / 'keep').read_text(), 'content')
        self.assertTrue((target / '.nested').is_dir())
        self.assertTrue((target / 'symlink').is_symlink())
        self.assertTrue((outside / 'empty').is_file())

    def test_empty_rejects_root_and_invalid_directory(self):
        for args in [('/',), ('--apply', '/'), ('missing',), ('--apply',)]:
            self.assertEqual(self.run_script('empty_files', *args).returncode, 2)

    def test_sizes_hidden_unusual_names_and_no_symlink_traversal(self):
        names = ['.hidden', 'two words', '-leading', 'line\nbreak']
        for name in names:
            (self.cwd / name).write_text('content')
        (self.cwd / 'broken').symlink_to('missing target')
        result = self.run_script('files_size')
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 5)
        for line in lines:
            size, name = line.split('\t', 1)
            self.assertTrue(size.isdecimal(), line)
            self.assertTrue(name)
        self.assertIn('.hidden', result.stdout)
        self.assertIn('two\\ words', result.stdout)

    def test_sizes_empty_directory_has_no_phantom_glob(self):
        self.ok('files_size', output='')

    def fake_ping(self, status):
        binary = self.cwd / 'ping'
        binary.write_text(f'#!/bin/sh\nprintf "%s\\n" "$@" > "$PING_RECORD"\nexit {status}\n')
        binary.chmod(0o755)
        return {'PATH': str(self.cwd), 'PING_RECORD': str(self.cwd / 'record')}

    def test_host_success_records_exact_safe_arguments(self):
        self.ok('host_status', '192.0.2.1', output='ICMP reply: 192.0.2.1\n', env=self.fake_ping(0))
        self.assertEqual((self.cwd / 'record').read_text().splitlines(),
                         ['-n', '-c', '1', '-W', '2', '--', '192.0.2.1'])

    def test_host_no_reply_and_probe_error_are_distinct(self):
        for status, expected in [(1, 1), (2, 2), (127, 2)]:
            result = self.run_script('host_status', 'example.invalid', env=self.fake_ping(status))
            self.assertEqual(result.returncode, expected)
            self.assertTrue(result.stdout if expected == 1 else result.stderr)

    def test_host_missing_ping_and_invalid_inputs(self):
        self.assertEqual(self.run_script('host_status', '192.0.2.1', env={'PATH': str(self.cwd)}).returncode, 2)
        for host in ['-c', '', 'host name', '$(touch INJECTED)', 'a;id']:
            self.assertEqual(self.run_script('host_status', host).returncode, 2)
        self.assertFalse((self.cwd / 'INJECTED').exists())


if __name__ == '__main__':
    unittest.main()
