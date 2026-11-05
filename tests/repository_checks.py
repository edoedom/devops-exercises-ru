"""Статические проверки; они не заменяют Terraform validate и кластер Kubernetes."""
import ast
from pathlib import Path
import sys

import hcl2
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tests"))
import syntax_lint  # noqa: E402


def main():
    counts = {"python": 0, "yaml": 0, "hcl": 0, "markdown": 0}
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if any(part.startswith(".") or part in {"__pycache__", "node_modules", "venv", "challenge_venv"}
               for part in relative.parts) or not path.is_file():
            continue
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=str(relative))
            counts["python"] += 1
        elif path.suffix in {".yml", ".yaml"}:
            list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
            counts["yaml"] += 1
        elif path.suffix == ".tf":
            with path.open(encoding="utf-8") as stream:
                hcl2.load(stream)
            counts["hcl"] += 1
        elif path.suffix == ".md" and relative.parts[0] != "tests":
            syntax_lint.errors.clear()
            syntax_lint.check_md_file(path)
            if syntax_lint.errors:
                raise AssertionError(f"{relative}: {syntax_lint.errors}")
            counts["markdown"] += 1
    print("Static checks:", counts)


if __name__ == "__main__":
    main()
