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
    for files in allFilesinFolders:
        # Source file
        sourceFile = os.path.join(os.path.join(initialDirectoryName,folders), files)        

        ###########################
        # Change 'png' to the name of the directory you want to create the output files
        ###########################        

        # Check if directory exists or not
        if not os.path.exists(os.path.join(initialDirectoryName, folders + '/png')):
            os.makedirs(os.path.join(initialDirectoryName, folders + '/png'))        
        # Destination file
        destFile = os.path.join(os.path.join(initialDirectoryName,folders + '/png'), files[:-4] + '.png')        
        # Convert file
        os.system('convert ' + sourceFile + ' ' + destFile)