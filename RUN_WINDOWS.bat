@echo off
cd /d "%~dp0"
set "PYTHON=%~dp0.venv\Scripts\python.exe"
if not exist "%PYTHON%" (
    echo Virtual environment not found.
    echo Run: python -m venv .venv
    echo Then run: .venv\Scripts\python.exe -m pip install -r requirements.txt
    pause
    exit /b 1
)
"%PYTHON%" -m src.train
if errorlevel 1 (
    pause
    exit /b 1
)
"%PYTHON%" app.py
pause
