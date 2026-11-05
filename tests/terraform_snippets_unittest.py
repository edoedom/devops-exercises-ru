"""Parse complete HCL examples in the Terraform tutorial, including question text."""
from pathlib import Path
import re
import unittest

import hcl2


class TerraformSnippets(unittest.TestCase):
    def test_complete_configuration_blocks_parse(self):
        path = Path(__file__).resolve().parents[1] / 'topics/terraform/README.md'
        # HTML details blocks contain fences too, so extract fences directly.
        snippets = re.finditer(r'```[^\n]*\n(.*?)```', path.read_text(), re.S)
        checked = 0
        for match in snippets:
            code = match.group(1)
            if not re.match(r'\s*(resource|data|variable|output|locals|terraform|provider|module)\s*["{]', code):
                continue
            # Explicitly abbreviated teaching fragments are not complete HCL.
            if re.search(r'^\s*\.\.\.\s*$', code, re.M):
                continue
            checked += 1
            with self.subTest(block=checked, code=code):
                hcl2.loads(code)
        self.assertGreater(checked, 0, 'No Terraform examples found')


if __name__ == '__main__':
    unittest.main()
