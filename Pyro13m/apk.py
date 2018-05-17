import os


initialDirectory = "/home/priyom/random/"


os.chdir(initialDirectory)
directorylist=os.listdir(initialDirectory)

for files in directorylist:

	os.system('adb install '+files)
