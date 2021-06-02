:: https://ss64.com/nt/syntax-variables.html

cd app

set LAUNCHED=F
set PYTHON_FOLDER_NEWEST=%LocalAppData%\Programs\Python\Python39-32
set PYTHON_FOLDER=%LocalAppData%\Programs\Python\Python38-32
set PYTHON_FOLDER_64=%LocalAppData%\Programs\Python\Python38
set PYTHON_FOLDER_OLD=%HOMEDRIVE%\Python34

:: Look for Python 3.9.x 32-bit
:: where python.exe  # doesn't work on XP
if defined LocalAppData (
    if exist %PYTHON_FOLDER_NEWEST%\python.exe (
        rem Python 3.9.x found!
        set LAUNCHED=T
        %PYTHON_FOLDER_NEWEST%\python.exe server.py
    )
)

:: Look for Python 3.8.x 32-bit
if defined LocalAppData (
    if exist %PYTHON_FOLDER%\python.exe (
        rem Python 3.8.x found!
        set LAUNCHED=T
        %PYTHON_FOLDER%\python.exe server.py
    )
)

:: Look for Python 3.8.x 64-bit
if defined LocalAppData (
    if exist %PYTHON_FOLDER_64%\python.exe (
        rem Python 3.8.x found!
        set LAUNCHED=T
        %PYTHON_FOLDER_64%\python.exe server.py
    )
)
:: Look for Python 3.4.x
if "%LAUNCHED%"=="F" (
    rem Looking for Python 3.4.x
    if exist %PYTHON_FOLDER_OLD%\python.exe (
        rem Python 3.4.x found!
        set LAUNCHED=T
        %PYTHON_FOLDER_OLD%\python.exe server.py
    )
)

:: Look for Python in PATH
if "%LAUNCHED%"=="F" (
    rem Looking for Python in PATH
    set LAUNCHED=T
    python server.py
)

@pause
