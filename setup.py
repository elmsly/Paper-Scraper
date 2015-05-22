import sys
import subprocess

print "Installing requirements"
try:
	subprocess.call(["pip", "install", "-r", "requirements.txt"])
except:
	raise Exception("Pip is required to continue. Please run 'sudo easy_install pip'")
	sys.exit()

subprocess.call(["python", "PS_DBgen.py"])