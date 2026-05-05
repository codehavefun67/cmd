@echo off
setlocal enabledelayedexpansion

echo ====================================================
echo           TOTAL OUTPUT CONTROL COMPILER
echo ====================================================
echo.

:GET_FILE_PATH
set /p USER_PATH="1. Enter full path to .py file: "
set "USER_PATH=%USER_PATH:"=%"

if not exist "%USER_PATH%" (
    echo [ERROR] Python file not found.
    goto GET_FILE_PATH
)

:GET_SAVE_PATH
echo.
set /p SAVE_PATH="2. Enter the target folder for all outputs: "
set "SAVE_PATH=%SAVE_PATH:"=%"

:: Create the master folder if it doesn't exist
if not exist "%SAVE_PATH%" mkdir "%SAVE_PATH%"

for %%i in ("%USER_PATH%") do set FILENAME=%%~ni

echo.
echo ----------------------------------------------------
echo ^> Source: %USER_PATH%
echo ^> Target: %SAVE_PATH%
echo ----------------------------------------------------

:: Pointing all internal PyInstaller paths to your chosen folder
pyinstaller --onefile --windowed --noconfirm ^
    --name "%FILENAME%" ^
    --specpath "%SAVE_PATH%" ^
    --workpath "%SAVE_PATH%\build" ^
    --distpath "%SAVE_PATH%\dist" ^
    "%USER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo SUCCESS! 
    echo.
    echo [EXE Location]   -> %SAVE_PATH%\dist\
    echo [Build Folder]   -> %SAVE_PATH%\build\
    echo [Spec File]      -> %SAVE_PATH%\%FILENAME%.spec
    echo ====================================================
    start "" "%SAVE_PATH%"
) else (
    echo.
    echo [ERROR] Compilation failed.
)

pause >nul
