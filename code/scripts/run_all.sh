#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting full suite of BERT experiments using venv2..."
bash "${SCRIPT_DIR}/run_execution_status.sh"
bash "${SCRIPT_DIR}/run_response_category.sh"
echo "All experiments finished successfully!"
