import os

# Find all directory names
initialDirectoryName = 'pictures'
allDirectories = os.listdir(initialDirectoryName)

print allDirectories

for folders in allDirectories:
	# Print foldername
	print "Files inside folder: " + folders

	# Go inside the corresponding folder
	fullPath = os.path.join(initialDirectoryName, folders)

	# Print all files inside the folder
	allFilesinFolders = os.listdir(fullPath)
	print allFilesinFolders

	# Copy to some other directory
	# os.system('convert <source> pictures/<folderName>/output/<filename.png>')
	for files in allFilesinFolders:
		print files