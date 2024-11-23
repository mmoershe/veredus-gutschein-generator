@echo off
cls

echo Checking if VENV exists...
if exist venv (
    echo ...it already exists!
)   else (
    echo ...it doesn't exist, venv will be created. Hold on...
    python -m venv venv
    echo ...Done!
)

echo Activating VENV
call venv\Scripts\activate
python.exe -m pip install --upgrade pip 
pip install -r requirements.txt
pip freeze 
python main.py 
