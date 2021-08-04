# quick installer for Jovian Framework

from __future__ import print_function
import subprocess
import os

print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
    
print("")
print("")

print("[*] Installing Jovian Framework to C:\Windows\System32")
print(os.getcwd())

subprocess.Popen("mkdir C:\Windows\System32\jktool;xcopy * C:\Windows\System32\jktool;", shell=True).wait()

print("")
print("")

print("[*] Creating launcher for jktool...")

filewrite = open("C:\Windows\System32\jktool", "w")
filewrite.write("#!/bin/sh\ncd C:\Windows\System32\jktool\npython jovian.py")
filewrite.close()

print("")
print("")

print("[*] Finished. Run 'jktool' to start the Jovian Framework.")
