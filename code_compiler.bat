@echo off
setlocal enabledelayedexpansion

echo ----------------------------------------------------
echo           PYTHON TO EXE COMPILER (Manual)
echo ----------------------------------------------------
echo.

:GET_FILE
:: 1. Ask the user for the file name
set /p TARGET="Enter the full filename (e.g., myscript.py): "

:: 2. Check if the file exists
if not exist "%TARGET%" (
    echo [ERROR] File "%TARGET%" not found in this folder.
    echo Please try again.
    echo.
    goto GET_FILE
)

:: 3. Ask for the output name (Optional)
set /p EXE_NAME="Enter the desired name for your EXE (press Enter for default): "

:: If the user just hits enter, use the script's name
if "%EXE_NAME%"=="" (
    set EXE_NAME=%~n1
)

echo.
echo ^> Compiling %TARGET% into %EXE_NAME%.exe...
echo ----------------------------------------------------

:: 4. Run PyInstaller
pyinstaller --onefile --name "%EXE_NAME%" "%TARGET%"

:: 5. Success check
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Compilation finished. Your EXE is in the 'dist' folder.
) else (
    echo.
    echo [ERROR] Compilation failed. Check the logs above.
)

pause