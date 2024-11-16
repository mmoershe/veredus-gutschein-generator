@echo off
cls
echo start

echo Checking if VENV exists...
if exist venv (
    echo ...it already exists!
)   else (
    echo ...it doesn't exist, venv will be created. Hold on...
    python -m venv venv
    rem install requirements.txt stuff
    echo ...Done!
)
call venv\Scripts\activate
pip install -r requirements.txt
pip freeze 
python main.py 
pause