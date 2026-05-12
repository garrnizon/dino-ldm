#! /bin/bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

# git clone https://github.com/facebookresearch/dinov3.git
# rm -rf dinov3/.git

# git clone https://github.com/shiml20/SVG.git
# rm -rf SVG/.git

python3 -m venv venv_vis
venv_vis/bin/pip install -r src/exp/visualizations/requirements.txt

venv_vis/bin/python src/setup/setup.py


