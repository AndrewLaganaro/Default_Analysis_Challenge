@echo off
set ENV_PATH=Python\ds-challenge
set REQ_PATH=requirements.txt

python -m venv %ENV_PATH%
%ENV_PATH%\Scripts\pip install -r %REQ_PATH%