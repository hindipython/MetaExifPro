@echo off
echo ===================================================
echo   MetaExif Pro - Clean Build System
echo ===================================================
echo.
echo 1. Creating isolated Virtual Environment...
python -m venv .build_env

echo.
echo 2. Installing dependencies into isolated environment...
call .build_env\Scripts\activate
pip install -r requirements.txt
echo.
echo 2. Installing dependencies into isolated environment...
call .build_env\Scripts\activate
pip install -r requirements.txt
pip install pyinstaller

echo.
echo 3. Generating Icon...
python generate_icon.py

echo.
echo 4. Starting Compilation (Minimizing Size)...
python build.py

echo.
echo ===================================================
echo   Done! Your file is in the 'dist' folder.
echo ===================================================
pause
