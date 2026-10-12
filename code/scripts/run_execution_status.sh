#!/usr/bin/env bash
set -e

VENV_PYTHON="/home/eshwar/code/simulator_persuasion/code/venv2/bin/python"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

echo "=========================================================="
echo " Training Execution Status Classifiers with venv2"
echo " Python: ${VENV_PYTHON}"
echo "=========================================================="

echo "[1/2] Training on dataset_2..."
${VENV_PYTHON} "${ROOT_DIR}/code/scripts/train.py" \
  --config "${ROOT_DIR}/code/configs/execution_status/dataset_2.yaml"

echo "[2/2] Training on combined (dataset_2 + srcc)..."
${VENV_PYTHON} "${ROOT_DIR}/code/scripts/train.py" \
  --config "${ROOT_DIR}/code/configs/execution_status/combined.yaml"

echo "Done! Models and reports saved in code/models/ and code/reports/."
