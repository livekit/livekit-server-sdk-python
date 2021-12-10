#!/usr/bin/env bash
set -euo pipefail

cd "$( dirname "$( dirname "${BASH_SOURCE[0]}" )" )"
source bin/lib.sh

log_info "Formatting"
black .

log_info "Sorting imports"
isort .
