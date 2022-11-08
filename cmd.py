import os
from sys import platform

if platform == "linux" or platform == "linux2":
    os.system("pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu")
elif platform == "win32" or platform == "darwin":
    os.system("pip3 install torch torchaudio torchvision")

os.system("pip install -r requirements.txt")