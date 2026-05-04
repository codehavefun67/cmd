@echo off
setlocal enabledelayedexpansion

echo ====================================================
echo             PYINSTALLER PATH COMPILER
echo ====================================================
echo.
echo TIP: You can right-click in this window to paste a path,
echo      or drag the file directly into this window.
echo.

:GET_PATH
set /p USER_PATH="Enter full path to .py file: "

:: Remove any quotes the user might have included in their paste
set "USER_PATH=%USER_PATH:"=%"

:: Check if the file exists
if not exist "%USER_PATH%" (
    echo.
    echo [ERROR] Could not find file at: "%USER_PATH%"
    echo Please check the path and try again.
    echo.
    goto GET_PATH
)

echo.
echo [FOUND] %USER_PATH%
echo ----------------------------------------------------
echo.

:: Extract the filename without extension for the EXE name
for %%i in ("%USER_PATH%") do set FILENAME=%%~ni

echo ^> Compiling...
:: Using quotes around %USER_PATH% ensures it works with spaces
pyinstaller --onefile --windowed --name "%FILENAME%" "%USER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo SUCCESS: %FILENAME%.exe created in the 'dist' folder.
    echo ====================================================
    :: Open the dist folder automatically
    start "" "dist"
) else (
    echo.
    echo [ERROR] Something went wrong during compilation.
)

echo.
echo Press any key to exit...
pause >nul
