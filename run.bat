@echo off
cls
echo start

set "VENV_NAME=gift-venv"

echo Checking if VENV exists...
if exist %VENV_NAME% (
    echo ...it already exists!
)   else (
    echo ...it doesn't exist, venv with the name %VENV_NAME% will be created. Hold on...
    python -m venv %VENV_NAME%
    rem install requirements.txt stuff
    echo ...Done!
)

