import subprocess
import sys
import os

venv_path = os.path.abspath('..\\env\\Scripts\\activate')

if sys.platform.startswith('win'):
    activate_script = 'activate'
else:
    activate_script = 'activate'

activate_cmd = f'"{venv_path}" && {activate_script}'

try:
    subprocess.run(activate_cmd, shell=True, check=True)
    print("Virtual environment ativado com sucesso.")
except subprocess.CalledProcessError:
    print("Erro ao ativar o virtual environment.")
