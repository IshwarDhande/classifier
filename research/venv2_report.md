# Python Environment Audit Report

**Virtual environment:** `/home/eshwar/code/simulator_persuasion/code/venv2`
**Project directory:** `/home/eshwar/code/simulator_persuasion/code`
**Report compiled:** 2026-10-12

## 1. Executive Summary

- Python version: **3.12.3**
- PyTorch: **2.14.1**
- Transformers: **5.18.0**
- Gymnasium: **1.4.0**
- Stable-Baselines3: **2.9.0**
- Dependency check: **No broken requirements found**
- CUDA availability reported by PyTorch: **False**
- PyTorch CUDA build: **13.0**
- `sentence-transformers`, `scikit-learn`, and `mujoco`: **not installed**

**Interpretation:** The environment has a core PyTorch/Transformers/RL stack and reports no pip dependency conflicts. However, CUDA is not currently available to PyTorch, and several packages that may be needed for classifier experiments or MuJoCo simulation are absent. The CUDA build version alone does not establish that a usable NVIDIA GPU/driver is available.

## 2. Python and Environment Details

```text
Python: 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]
Executable: /home/eshwar/code/simulator_persuasion/code/venv2/bin/python
torch: 2.14.1
transformers: 5.18.0
sentence-transformers: NOT INSTALLED
numpy: 2.5.3
pandas: 2.3.3
scikit-learn: NOT INSTALLED
gymnasium: 1.4.0
stable-baselines3: 2.9.0
pytest: 8.4.2
mujoco: NOT INSTALLED
CUDA available: False
PyTorch CUDA build: 13.0
```

## 3. ML, NLP, RL, and Research Package Status

| Package | Installed version / status |
|---|---|

### PyTorch / CUDA diagnostic

```text
Python: 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]
Executable: /home/eshwar/code/simulator_persuasion/code/venv2/bin/python
torch: 2.14.1
transformers: 5.18.0
sentence-transformers: NOT INSTALLED
numpy: 2.5.3
pandas: 2.3.3
scikit-learn: NOT INSTALLED
gymnasium: 1.4.0
stable-baselines3: 2.9.0
pytest: 8.4.2
mujoco: NOT INSTALLED
CUDA available: False
PyTorch CUDA build: 13.0
```

### Optional library import tests

```text
No optional import-test results were present in the supplied report.
```

## 4. Dependency Health

```text
No broken requirements found.
```

## 5. Complete Installed Package Inventory

Total package rows parsed from `packages.txt`: **165**

| Package | Version |
|---|---|
| `absl-py` | `2.5.0` |
| `annotated-doc` | `0.0.5` |
| `anyio` | `4.15.1` |
| `argon2-cffi` | `25.1.0` |
| `argon2-cffi-bindings` | `26.1.0` |
| `arrow` | `1.4.0` |
| `asttokens` | `3.0.2` |
| `async-lru` | `2.3.0` |
| `attrs` | `26.1.0` |
| `babel` | `2.18.0` |
| `beautifulsoup4` | `4.15.0` |
| `black` | `25.12.0` |
| `bleach` | `6.4.0` |
| `certifi` | `2026.7.22` |
| `cffi` | `2.1.1` |
| `charset-normalizer` | `3.5.2` |
| `click` | `8.5.0` |
| `cloudpickle` | `3.1.2` |
| `comm` | `0.2.3` |
| `contourpy` | `1.4.0` |
| `cuda-bindings` | `13.4.3` |
| `cuda-pathfinder` | `1.8.3` |
| `cuda-toolkit` | `13.0.3.0` |
| `cycler` | `0.12.1` |
| `debugpy` | `1.8.22` |
| `defusedxml` | `0.7.1` |
| `executing` | `2.2.1` |
| `Farama-Notifications` | `0.0.6` |
| `fastjsonschema` | `2.22.2` |
| `filelock` | `4.0.12` |
| `flake8` | `7.4.1` |
| `fonttools` | `4.66.1` |
| `fqdn` | `1.6.0` |
| `fsspec` | `2026.9.0` |
| `grpcio` | `1.84.0` |
| `gymnasium` | `1.4.0` |
| `h11` | `0.16.0` |
| `hf-xet` | `1.6.0` |
| `httpcore` | `1.0.9` |
| `httpx` | `0.28.1` |
| `huggingface_hub` | `1.33.0` |
| `idna` | `3.20` |
| `iniconfig` | `2.3.0` |
| `ipykernel` | `6.31.0` |
| `ipython` | `9.17.1` |
| `ipython_pygments_lexers` | `1.1.1` |
| `isoduration` | `20.11.0` |
| `isort` | `6.1.0` |
| `jedi` | `0.20.0` |
| `Jinja2` | `3.1.6` |
| `json5` | `0.15.0` |
| `jsonpointer` | `3.1.1` |
| `jsonschema` | `4.26.0` |
| `jupyter_builder` | `1.2.3` |
| `jupyter_client` | `8.10.0` |
| `jupyter_core` | `5.9.1` |
| `jupyter-events` | `0.12.1` |
| `jupyter-lsp` | `2.3.1` |
| `jupyter_server` | `2.21.1` |
| `jupyter_server_terminals` | `0.5.4` |
| `jupyterlab` | `4.6.4` |
| `jupyterlab_pygments` | `0.3.0` |
| `jupyterlab_server` | `2.28.1` |
| `kiwisolver` | `1.5.1` |
| `lark` | `1.3.1` |
| `Markdown` | `3.11` |
| `markdown-it-py` | `4.2.0` |
| `MarkupSafe` | `3.0.4` |
| `matplotlib` | `3.11.2` |
| `matplotlib-inline` | `0.2.2` |
| `mccabe` | `0.7.0` |
| `mdurl` | `0.1.2` |
| `mistune` | `3.3.4` |
| `mpmath` | `1.3.0` |
| `mypy_extensions` | `1.1.0` |
| `nbclient` | `0.11.0` |
| `nbconvert` | `7.17.1` |
| `nbformat` | `5.11.1` |
| `nest-asyncio` | `1.6.0` |
| `networkx` | `3.7` |
| `notebook_shim` | `0.2.4` |
| `numpy` | `2.5.3` |
| `nvidia-cublas` | `13.1.1.3` |
| `nvidia-cuda-cupti` | `13.0.85` |
| `nvidia-cuda-nvrtc` | `13.0.88` |
| `nvidia-cuda-runtime` | `13.0.96` |
| `nvidia-cudnn-cu13` | `9.24.0.43` |
| `nvidia-cufft` | `12.0.0.61` |
| `nvidia-cufile` | `1.15.1.6` |
| `nvidia-curand` | `10.4.0.35` |
| `nvidia-cusolver` | `12.0.4.66` |
| `nvidia-cusparse` | `12.6.3.3` |
| `nvidia-cusparselt-cu13` | `0.8.1` |
| `nvidia-nccl-cu13` | `2.30.7` |
| `nvidia-nvjitlink` | `13.4.92` |
| `nvidia-nvshmem-cu13` | `3.4.5` |
| `nvidia-nvtx` | `13.0.85` |
| `packaging` | `26.3` |
| `pandas` | `2.3.3` |
| `pandocfilters` | `1.5.1` |
| `parso` | `0.8.7` |
| `pathspec` | `1.1.1` |
| `pexpect` | `4.9.0` |
| `pillow` | `12.3.0` |
| `pip` | `24.0` |
| `platformdirs` | `4.12.3` |
| `pluggy` | `1.6.0` |
| `prometheus_client` | `0.26.0` |
| `prompt_toolkit` | `3.0.53` |
| `protobuf` | `7.36.2` |
| `psutil` | `7.2.2` |
| `ptyprocess` | `0.7.0` |
| `pure_eval` | `0.2.4` |
| `pycodestyle` | `2.15.0` |
| `pycparser` | `3.0` |
| `pyflakes` | `4.0.2` |
| `Pygments` | `2.21.0` |
| `pyparsing` | `3.3.3` |
| `pytest` | `8.4.2` |
| `python-dateutil` | `2.9.0.post0` |
| `python-json-logger` | `4.2.0` |
| `pytokens` | `0.4.1` |
| `pytz` | `2026.5` |
| `PyYAML` | `6.0.3` |
| `pyzmq` | `27.2.0` |
| `referencing` | `0.37.0` |
| `regex` | `2026.9.29` |
| `requests` | `2.34.2` |
| `rfc3339-validator` | `0.1.4` |
| `rfc3986-validator` | `0.1.1` |
| `rfc3987-syntax` | `1.1.0` |
| `rich` | `15.0.0` |
| `rpds-py` | `2026.9.1` |
| `safetensors` | `0.8.0` |
| `Send2Trash` | `2.1.0` |
| `setuptools` | `84.0.0` |
| `shellingham` | `1.5.4` |
| `six` | `1.17.0` |
| `soupsieve` | `2.10` |
| `stable_baselines3` | `2.9.0` |
| `stack-data` | `0.6.3` |
| `sympy` | `1.14.0` |
| `tensorboard` | `2.21.0` |
| `tensorboard-data-server` | `0.7.2` |
| `terminado` | `0.18.1` |
| `tinycss2` | `1.5.1` |
| `tokenizers` | `0.23.2` |
| `torch` | `2.14.1` |
| `torchaudio` | `2.11.0` |
| `torchvision` | `0.29.1` |
| `tornado` | `6.5.10` |
| `tqdm` | `4.70.1` |
| `traitlets` | `5.16.1` |
| `transformers` | `5.18.0` |
| `triton` | `3.8.0` |
| `typer` | `0.27.2` |
| `typing_extensions` | `4.16.0` |
| `tzdata` | `2026.5` |
| `uri-template` | `1.3.0` |
| `urllib3` | `2.8.0` |
| `wcwidth` | `0.9.2` |
| `webcolors` | `25.10.0` |
| `webencodings` | `0.6.1` |
| `websocket-client` | `1.9.2` |
| `Werkzeug` | `3.1.9` |

## 6. Pinned Requirements Snapshot

The following entries preserve the supplied `pip freeze` output for reproducibility.

```text
absl-py==2.5.0
annotated-doc==0.0.5
anyio==4.15.1
argon2-cffi==25.1.0
argon2-cffi-bindings==26.1.0
arrow==1.4.0
asttokens==3.0.2
async-lru==2.3.0
attrs==26.1.0
babel==2.18.0
beautifulsoup4==4.15.0
black==25.12.0
bleach==6.4.0
certifi==2026.7.22
cffi==2.1.1
charset-normalizer==3.5.2
click==8.5.0
cloudpickle==3.1.2
comm==0.2.3
contourpy==1.4.0
cuda-bindings==13.4.3
cuda-pathfinder==1.8.3
cuda-toolkit==13.0.3.0
cycler==0.12.1
debugpy==1.8.22
defusedxml==0.7.1
executing==2.2.1
Farama-Notifications==0.0.6
fastjsonschema==2.22.2
filelock==4.0.12
flake8==7.4.1
fonttools==4.66.1
fqdn==1.6.0
fsspec==2026.9.0
grpcio==1.84.0
gymnasium==1.4.0
h11==0.16.0
hf-xet==1.6.0
httpcore==1.0.9
httpx==0.28.1
huggingface_hub==1.33.0
idna==3.20
iniconfig==2.3.0
ipykernel==6.31.0
ipython==9.17.1
ipython_pygments_lexers==1.1.1
isoduration==20.11.0
isort==6.1.0
jedi==0.20.0
Jinja2==3.1.6
json5==0.15.0
jsonpointer==3.1.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
jupyter-events==0.12.1
jupyter-lsp==2.3.1
jupyter_builder==1.2.3
jupyter_client==8.10.0
jupyter_core==5.9.1
jupyter_server==2.21.1
jupyter_server_terminals==0.5.4
jupyterlab==4.6.4
jupyterlab_pygments==0.3.0
jupyterlab_server==2.28.1
kiwisolver==1.5.1
lark==1.3.1
Markdown==3.11
markdown-it-py==4.2.0
MarkupSafe==3.0.4
matplotlib==3.11.2
matplotlib-inline==0.2.2
mccabe==0.7.0
mdurl==0.1.2
mistune==3.3.4
mpmath==1.3.0
mypy_extensions==1.1.0
nbclient==0.11.0
nbconvert==7.17.1
nbformat==5.11.1
nest-asyncio==1.6.0
networkx==3.7
notebook_shim==0.2.4
numpy==2.5.3
nvidia-cublas==13.1.1.3
nvidia-cuda-cupti==13.0.85
nvidia-cuda-nvrtc==13.0.88
nvidia-cuda-runtime==13.0.96
nvidia-cudnn-cu13==9.24.0.43
nvidia-cufft==12.0.0.61
nvidia-cufile==1.15.1.6
nvidia-curand==10.4.0.35
nvidia-cusolver==12.0.4.66
nvidia-cusparse==12.6.3.3
nvidia-cusparselt-cu13==0.8.1
nvidia-nccl-cu13==2.30.7
nvidia-nvjitlink==13.4.92
nvidia-nvshmem-cu13==3.4.5
nvidia-nvtx==13.0.85
packaging==26.3
pandas==2.3.3
pandocfilters==1.5.1
parso==0.8.7
pathspec==1.1.1
pexpect==4.9.0
pillow==12.3.0
platformdirs==4.12.3
pluggy==1.6.0
prometheus_client==0.26.0
prompt_toolkit==3.0.53
protobuf==7.36.2
psutil==7.2.2
ptyprocess==0.7.0
pure_eval==0.2.4
pycodestyle==2.15.0
pycparser==3.0
pyflakes==4.0.2
Pygments==2.21.0
pyparsing==3.3.3
pytest==8.4.2
python-dateutil==2.9.0.post0
python-json-logger==4.2.0
pytokens==0.4.1
pytz==2026.5
PyYAML==6.0.3
pyzmq==27.2.0
referencing==0.37.0
regex==2026.9.29
requests==2.34.2
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rfc3987-syntax==1.1.0
rich==15.0.0
rpds-py==2026.9.1
safetensors==0.8.0
Send2Trash==2.1.0
setuptools==84.0.0
shellingham==1.5.4
six==1.17.0
soupsieve==2.10
stable_baselines3==2.9.0
stack-data==0.6.3
sympy==1.14.0
tensorboard==2.21.0
tensorboard-data-server==0.7.2
terminado==0.18.1
tinycss2==1.5.1
tokenizers==0.23.2
torch==2.14.1
torchaudio==2.11.0
torchvision==0.29.1
tornado==6.5.10
tqdm==4.70.1
traitlets==5.16.1
transformers==5.18.0
triton==3.8.0
typer==0.27.2
typing_extensions==4.16.0
tzdata==2026.5
uri-template==1.3.0
urllib3==2.8.0
wcwidth==0.9.2
webcolors==25.10.0
webencodings==0.6.1
websocket-client==1.9.2
Werkzeug==3.1.9
```

## 7. Research-Relevant Findings

1. **Barrier-classifier experiments:** `transformers` and PyTorch are installed. `scikit-learn` is not installed, so Logistic Regression, standard classification metrics, and related sklearn utilities will require it.
2. **Sentence embedding experiments:** `sentence-transformers` is not installed. It is needed for the proposed `all-MiniLM-L6-v2` sentence-embedding workflow; alternatively, the Hugging Face Transformers API can be used directly.
3. **RL experiments:** `gymnasium` and `stable-baselines3` are installed. Confirm compatibility with the simulator's own requirements and tests before changing versions.
4. **MuJoCo:** the `mujoco` Python package is not installed according to the supplied package audit. Install it only if this environment needs to run MuJoCo-based experiments.
5. **GPU acceleration:** PyTorch reports CUDA unavailable despite being a CUDA build. Check `nvidia-smi`, GPU visibility, and driver/runtime compatibility before attempting GPU training.
6. **Dependency consistency:** `pip check` reports no broken requirements. This does not guarantee that every package works at runtime or that the project-specific test suite passes.

## 8. Recommended Next Checks

Run these from the activated environment before making changes:

```bash
source /home/eshwar/code/simulator_persuasion/code/venv2/bin/activate
nvidia-smi
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.version.cuda)"
python -m pytest
```

Run the project test command appropriate to the repository; `python -m pytest` is a broad example and may take time.

## 9. Source Files Combined

- `ml_stack.txt` — Python and ML/RL stack diagnostics
- `dependency_check.txt` — pip dependency consistency output
- `packages.txt` — installed package table
- `requirements.txt` — pinned package snapshot

---

*This report consolidates the supplied audit outputs. It does not modify or install anything in the virtual environment.*
