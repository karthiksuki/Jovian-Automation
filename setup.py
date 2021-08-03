# quick installer for Jovian Framework

from __future__ import print_function
import subprocess
import os

print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()

if os.name == 'nt':
    os.system("pip install -r requirements.txt")
else:
    os.system("pip3 install -r requirements.txt")
    
print("")
print("")

print("[*] Installing Jovian Framework to /usr/share/jktool..")
print(os.getcwd())

subprocess.Popen("mkdir /usr/share/jktool/;mkdir /etc/jktool/;cp -rf * /usr/share/jktool/;cp src/core/config.baseline /etc/jktool/set.config", shell=True).wait()

print("")
print("")

print("[*] Creating launcher for jktool...")

filewrite = open("/usr/local/bin/jktool", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/jktool\npython3 jovian.py")
filewrite.close()

print("")
print("")

print("[*] Done. Chmoding +x.... ")
subprocess.Popen("chmod +x /usr/local/bin/jktool", shell=True).wait()


print("")
print("")

print("[*] Finished. Run 'jktool' to start the Jovian Framework.")











