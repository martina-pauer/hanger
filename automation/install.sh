#!/bin/bash
# Install All Dependencies For Run App
# Go to Repository Source Code root
cd /workspaces/hanger/src/
# Create Isolated Enviroment named ".venv"
python3 -m venv .venv
source .venv/bin/activate
pip3 install poetry==2.2.1
poetry install -E dev