#!/bin/bash

# install python packages
pip install uv
uv venv
uv pip install -r requirements.txt

# install model natural language model
uv run python -m spacy download en_core_web_lg
uv run python -m spacy download en_core_web_sm
