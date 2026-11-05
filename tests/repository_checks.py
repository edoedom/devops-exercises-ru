"""Статические проверки всех файлов проекта. Сеть и облачные операции не используются."""
import ast
import os
from pathlib import Path
import re
import sys
import subprocess

import hcl2
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tests'))
import syntax_lint  # noqa: E402


class UniqueSafeLoader(yaml.SafeLoader):
    """YAML с true/false вместо YAML 1.1 on/off и запретом дублирующихся ключей."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, expr) for tag, expr in values if tag != 'tag:yaml.org,2002:bool']
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
UniqueSafeLoader.add_implicit_resolver('tag:yaml.org,2002:bool',
                                     re.compile(r'^(?:true|false|True|False|TRUE|FALSE)$'), list('tTfF'))


def unique_mapping(loader, node, deep=False):
    explicit = set()
    for key_node, _ in node.value:
        if key_node.tag == 'tag:yaml.org,2002:merge':
            continue
        key = loader.construct_object(key_node, deep=deep)
        if key in explicit:
            raise ValueError(f'Duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}')
        explicit.add(key)
    loader.flatten_mapping(node)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(text):
    return list(yaml.load_all(text, Loader=UniqueSafeLoader))


def project_files(root):
    for directory, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if (not d.startswith('.') or d == '.github')
                         and d not in {'__pycache__', 'node_modules', 'venv', 'challenge_venv'})
        for name in sorted(names):
            yield Path(directory) / name


def main():
    counts = {'python': 0, 'yaml': 0, 'hcl': 0, 'markdown': 0, 'bash': 0}
    for path in project_files(ROOT):
        relative = path.relative_to(ROOT)
        if path.suffix == '.py':
            ast.parse(path.read_text(encoding='utf-8'), filename=str(relative))
            counts['python'] += 1
        elif path.suffix in {'.yml', '.yaml'}:
            load_yaml(path.read_text(encoding='utf-8'))
            counts['yaml'] += 1
        elif path.suffix == '.tf':
            with path.open(encoding='utf-8') as stream:
                hcl2.load(stream)
            counts['hcl'] += 1
        elif path.suffix == '.sh':
            subprocess.run(['bash', '-n', str(path)], check=True)
            counts['bash'] += 1
        elif path.suffix == '.md' and relative.parts[0] != 'tests':
            syntax_lint.check_md_file(path)
            if syntax_lint.errors:
                raise AssertionError(f'{relative}: {syntax_lint.errors}')
            counts['markdown'] += 1
    print('Static checks:', counts)


if __name__ == '__main__':
    main()
