#!/bin/bash
ENV_PATH="Python/ds-challenge"
REQ_PATH="requirements.txt"

python3 -m venv $ENV_PATH
$ENV_PATH/bin/pip install -r $REQ_PATH