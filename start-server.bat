@echo off
:: Starts IPIP-NEO-PI.
::
:: Detects the Windows version (XP, Vista, 7, 8, 8.1, 10, 11) and CPU type and
:: launches the matching standalone program, which needs no Python. Falls
:: back to the old Python version if no program file is found.
::
:: Must keep working on Windows XP: no "where", no PowerShell.
:: https://ss64.com/nt/syntax-variables.html

cd /d "%~dp0"

:: --- Windows version, e.g. "Microsoft Windows [Version 10.0.22631.4317]" ---
set VERSTR=
set MAJOR=0
set MINOR=0
set BUILD=0
for /f "tokens=2 delims=[]" %%a in ('ver') do set VERSTR=%%a
for /f "tokens=2,3,4 delims=. " %%a in ("%VERSTR%") do (
    set MAJOR=%%a
    set MINOR=%%b
    set BUILD=%%c
)

set WINNAME=Windows %MAJOR%.%MINOR%
if "%MAJOR%.%MINOR%"=="5.1" set WINNAME=Windows XP
if "%MAJOR%.%MINOR%"=="5.2" set WINNAME=Windows XP x64 / Server 2003
if "%MAJOR%.%MINOR%"=="6.0" set WINNAME=Windows Vista
if "%MAJOR%.%MINOR%"=="6.1" set WINNAME=Windows 7
if "%MAJOR%.%MINOR%"=="6.2" set WINNAME=Windows 8
if "%MAJOR%.%MINOR%"=="6.3" set WINNAME=Windows 8.1
if "%MAJOR%"=="10" set WINNAME=Windows 10
if "%MAJOR%"=="10" if %BUILD% GEQ 22000 set WINNAME=Windows 11

:: --- CPU type (PROCESSOR_ARCHITEW6432 is set inside 32-bit cmd.exe on 64-bit Windows) ---
set ARCH=%PROCESSOR_ARCHITECTURE%
if defined PROCESSOR_ARCHITEW6432 set ARCH=%PROCESSOR_ARCHITEW6432%

:: --- Pick the program ---
set LEGACY=IPIP-NEO-PI-WinXP-Win7-x86.exe
set PROGRAM=%LEGACY%
if %MAJOR% GEQ 10 (
    set PROGRAM=IPIP-NEO-PI-Win10-x86.exe
    if /i "%ARCH%"=="AMD64" set PROGRAM=IPIP-NEO-PI-Win10-x64.exe
    if /i "%ARCH%"=="ARM64" set PROGRAM=IPIP-NEO-PI-Win10-arm64.exe
)

echo Detected %WINNAME% (version %MAJOR%.%MINOR%.%BUILD%, %ARCH%)

:: Look next to this file, then in dist\windows (when built from source).
:: The legacy program also runs on Windows 10 / 11, so it is the fallback.
for %%d in (. dist\windows) do (
    if exist "%%d\%PROGRAM%" (
        echo Starting %PROGRAM% ...
        echo.
        "%%d\%PROGRAM%"
        goto :done
    )
)
for %%d in (. dist\windows) do (
    if exist "%%d\%LEGACY%" (
        echo Starting %LEGACY% ...
        echo.
        "%%d\%LEGACY%"
        goto :done
    )
)

echo.
echo Could not find %PROGRAM%.
echo Download it from https://github.com/kholia/IPIP-NEO-PI/releases and put it
echo in the same folder as this file. Trying the old Python version instead...
echo.

:: --- Fallback: the Python version in the app folder ---
cd app

set LAUNCHED=F
set PYTHON_FOLDER_NEWEST=%LocalAppData%\Programs\Python\Python39-32
set PYTHON_FOLDER=%LocalAppData%\Programs\Python\Python38-32
set PYTHON_FOLDER_64=%LocalAppData%\Programs\Python\Python38
set PYTHON_FOLDER_OLD=%HOMEDRIVE%\Python34

:: Look for Python 3.9.x 32-bit
if defined LocalAppData (
    if exist %PYTHON_FOLDER_NEWEST%\python.exe (
        set LAUNCHED=T
        %PYTHON_FOLDER_NEWEST%\python.exe server.py
    )
)

:: Look for Python 3.8.x 32-bit
if "%LAUNCHED%"=="F" if defined LocalAppData (
    if exist %PYTHON_FOLDER%\python.exe (
        set LAUNCHED=T
        %PYTHON_FOLDER%\python.exe server.py
    )
)

:: Look for Python 3.8.x 64-bit
if "%LAUNCHED%"=="F" if defined LocalAppData (
    if exist %PYTHON_FOLDER_64%\python.exe (
        set LAUNCHED=T
        %PYTHON_FOLDER_64%\python.exe server.py
    )
)

:: Look for Python 3.4.x
if "%LAUNCHED%"=="F" (
    if exist %PYTHON_FOLDER_OLD%\python.exe (
        set LAUNCHED=T
        %PYTHON_FOLDER_OLD%\python.exe server.py
    )
)

:: Look for Python in PATH
if "%LAUNCHED%"=="F" (
    set LAUNCHED=T
    python server.py
)

:done
pause
