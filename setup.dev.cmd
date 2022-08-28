py -3.10 -m venv --clear --upgrade-deps .venv
CALL .venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
   EXIT /B %ERRORLEVEL%
)

@REM python -m pip install --upgrade --require-virtualenv --editable .[dev]
@REM python -m pip freeze --exclude-editable > requirements.dev.txt && echo -e . >> requirements.dev.txt

python -m pip install -r requirements.dev.txt --require-virtualenv
EXIT /B %ERRORLEVEL%
