@echo off
setlocal enabledelayedexpansion

echo ====================================================
echo           COMPLETE PATH CONTROL COMPILER
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
set /p SAVE_PATH="2. Enter the folder to save EVERYTHING into: "
set "SAVE_PATH=%SAVE_PATH:"=%"

:: Create the master folder if it doesn't exist
if not exist "%SAVE_PATH%" mkdir "%SAVE_PATH%"

:: Define sub-folders to keep it organized (Optional but recommended)
set "DIST_DIR=%SAVE_PATH%\output"
set "BUILD_DIR=%SAVE_PATH%\temp_build"

for %%i in ("%USER_PATH%") do set FILENAME=%%~ni

echo.
echo ----------------------------------------------------
echo ^> Source: %USER_PATH%
echo ^> Target Directory: %SAVE_PATH%
echo ----------------------------------------------------

:: Execute PyInstaller with full path redirection
pyinstaller --onefile --windowed --noconfirm ^
    --name "%FILENAME%" ^
    --distpath "%DIST_DIR%" ^
    --workpath "%BUILD_DIR%" ^
    --specpath "%SAVE_PATH%" ^
    "%USER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo SUCCESS! 
    echo.
    echo EXE Location:  "%DIST_DIR%"
    echo Build Files:   "%BUILD_DIR%"
    echo Spec File:     "%SAVE_PATH%\%FILENAME%.spec"
    echo ====================================================
    start "" "%DIST_DIR%"
) else (
    echo.
    echo [ERROR] Compilation failed.
)

pause >nul
