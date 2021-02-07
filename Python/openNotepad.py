import subprocess as sp

name = "notepad.exe"
fileName = "file.txt"
sp.Popen([name, fileName])