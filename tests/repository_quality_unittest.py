from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tests.repository_checks import load_yaml, project_files


class YamlQuality(unittest.TestCase):
    def test_duplicate_keys_cannot_silently_override_settings(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate YAML key'):
            load_yaml('spec:\n  replicas: 3\n  replicas: 0\n')

    def test_actions_on_is_a_key_and_booleans_remain_booleans(self):
        document = load_yaml('on:\n  push:\nflag: false\n')[0]
        self.assertIn('on', document)
        self.assertIs(document['flag'], False)

    def test_hidden_workflows_checked_but_venv_not_traversed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for p in ['.github/workflows/check.yml', '.venv/package/bad.py', 'tests/a.py']:
                f = root / p; f.parent.mkdir(parents=True, exist_ok=True); f.write_text('')
            found = {p.relative_to(root).as_posix() for p in project_files(root)}
        self.assertEqual(found, {'.github/workflows/check.yml', 'tests/a.py'})

    def test_explicit_override_of_yaml_merge_is_valid(self):
        document = load_yaml('defaults: &base\n  enabled: false\n  count: 1\n'
                             'app:\n  <<: *base\n  count: 2\n')[0]
        self.assertEqual(document['app'], {'enabled': False, 'count': 2})
