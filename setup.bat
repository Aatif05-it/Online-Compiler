@echo off
REM PyCompile Windows Setup & Run Script

echo.
echo 🐍 PyCompile - Python Compiler Setup
echo ====================================
echo.

REM Check Python
echo ✓ Checking Python installation...
python --version

REM Install dependencies
echo.
echo ✓ Installing backend dependencies...
cd backend
pip install -r requirements.txt -q
cd ..

REM Show instructions
echo.
echo ✓ Setup complete!
echo.
echo 📝 To run the application:
echo.
echo Step 1: Start Backend (Terminal 1)
echo   cd backend
echo   python main.py
echo.
echo Step 2: Start Frontend (Terminal 2)
echo   cd frontend
echo   python -m http.server 3000
echo.
echo Step 3: Open in Browser
echo   http://localhost:3000
echo.
echo Backend API docs: http://localhost:8000/docs
echo.
pause
