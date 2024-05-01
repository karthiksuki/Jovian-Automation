# quick installer for Jovian Framework
# Runs in windows

from __future__ import print_function
import subprocess
import os

print("[*] Installing requirements.txt...")
subprocess.Popen("pip install -r requirements.txt", shell=True).wait()
    
print("")
print("")

print("[*] Installation Completed")

print("")
print("")

print("[*] `python jovian.py` to start Jovian Framework")
