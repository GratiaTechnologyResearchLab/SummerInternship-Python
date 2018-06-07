import os

initialDirectory= "/home/SummerInternship/ArunavD/apkfiles/"


os.chdir(initialDirectory)
directorylist=os.listdr(initialDirectory)

for files in directorylist:

	os.system("adb install "+files)
	