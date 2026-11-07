#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"
# Match the shared fleet Markdown rules without an application dependency tree.
markdownlint-cli2 '*.md' 'docs/**/*.md' 'specs/**/*.md'
shellcheck scripts/check-development.sh
ruff check tests/test_workflow_security.py scripts/development-container.py tests/test_development_container.py tests/test_plot_files.py tests/test_plot_numerics.py GuppyScreen/scripts/plot_output.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 -m py_compile GuppyScreen/scripts/*.py
bash .githooks/pre-push
actionlint
zizmor --offline --min-severity medium --min-confidence medium .github
