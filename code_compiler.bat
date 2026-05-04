@echo off
setlocal enabledelayedexpansion

echo ====================================================
echo             PYINSTALLER PATH COMPILER
echo ====================================================
echo.
echo TIP: Right-click to paste or drag a file into this window.
echo.

:GET_PATH
set /p USER_PATH="Enter full path to .py file: "
set "USER_PATH=%USER_PATH:"=%"

if not exist "%USER_PATH%" (
    echo.
    echo [ERROR] Could not find file at: "%USER_PATH%"
    goto GET_PATH
)

for %%i in ("%USER_PATH%") do set FILENAME=%%~ni

echo.
echo ^> Compiling...
pyinstaller --onefile --windowed --noconfirm --name "%FILENAME%" "%USER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo SUCCESS: %FILENAME%.exe has been created.
    echo.
    echo SOURCE: %USER_PATH%
    echo EXPORT LOCATION: %~dp0dist\
    echo ====================================================
    if exist "dist" start "" "%~dp0dist"
) else (
    echo.
    echo [ERROR] Something went wrong during compilation.
)

echo.
echo Press any key to exit...
pause >nul
