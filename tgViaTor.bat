@ECHO OFF

:check_dir
SET script_dir=%~dp0

ECHO Script directory: %script_dir%

rem Replace "venv path" with the path of your Python venv
SET venv_path="%script_dir%TG_Tor_env"
ECHO venv_path : %venv_path%

:check_path

IF EXIST "%venv_path%" (
  GOTO activate_venv
) ELSE (
  ECHO Error: Virtual environment not found at "%venv_path%".
  PAUSE
  GOTO run_script
)

:run_script

rem Replace "your_script.py" with the name of your Python script
python "./tgViaTor.py"
PAUSE

GOTO end

:activate_venv
cd /d "%venv_path%/Scripts"
call activate.bat >nul
PAUSE
cd /d "%script_dir%"
GOTO run_script

:end

cls
PAUSE
