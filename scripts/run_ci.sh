#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"
python3 -m unittest discover -s tests -p '*_unittest.py' -v
python3 tests/repository_checks.py
python3 scripts/content_checks.py
python3 scripts/update_question_number.py --check
for exercise in flask_container_ci flask_container_ci2; do
  (cd "topics/$exercise" && python3 -m unittest tests app.tests -v)
done
