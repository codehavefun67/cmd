@echo off
setlocal enabledelayedexpansion

echo ====================================================
echo             PYINSTALLER CUSTOM PATH COMPILER
echo ====================================================
echo.

:GET_FILE_PATH
set /p USER_PATH="1. Enter full path to .py file: "
set "USER_PATH=%USER_PATH:"=%"

if not exist "%USER_PATH%" (
    echo [ERROR] File not found. Try again.
    goto GET_FILE_PATH
)

:GET_SAVE_PATH
echo.
set /p SAVE_PATH="2. Enter path where the EXE should be saved: "
set "SAVE_PATH=%SAVE_PATH:"=%"

:: Create the folder if it doesn't exist
if not exist "%SAVE_PATH%" (
    echo Folder does not exist. Creating it now...
    mkdir "%SAVE_PATH%"
)

for %%i in ("%USER_PATH%") do set FILENAME=%%~ni

echo.
echo ----------------------------------------------------
echo ^> Compiling: %FILENAME%
echo ^> Destination: %SAVE_PATH%
echo ----------------------------------------------------

:: --distpath: Specifies where to put the bundled app
:: --workpath: (Optional) Keeps the temporary build files in the save path too
pyinstaller --onefile --windowed --noconfirm ^
    --name "%FILENAME%" ^
    --distpath "%SAVE_PATH%" ^
    "%USER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo SUCCESS!
    echo YOUR EXE IS HERE: "%SAVE_PATH%\%FILENAME%.exe"
    echo ====================================================
    start "" "%SAVE_PATH%"
) else (
    echo.
    echo [ERROR] Compilation failed.
)

pause >nul
