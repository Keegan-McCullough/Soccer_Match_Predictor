import subprocess
import sys
import os

# 1. Create virtual environment
venv_dir = "venv"

if not os.path.exists(venv_dir):
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

# 2. Determine pip path based on OS
if os.name == "nt":
    pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
    python_path = os.path.join(venv_dir, "Scripts", "python.exe")
else:
    pip_path = os.path.join(venv_dir, "bin", "pip")
    python_path = os.path.join(venv_dir, "bin", "python")

# 3. Install requirements
subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
print("Installed dependencies")

# 4. Register kernel for Jupyter
subprocess.check_call([python_path, "-m", "ipykernel", "install", "--user", "--name=soccer-env", "--display-name", "Soccer Predictor"])