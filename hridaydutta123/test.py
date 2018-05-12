

# Read file 
with open('testfile.txt') as fr:
	content = fr.read()
	content1 = fr.readlines()

	# Show output of fr.read()
	print content

	# Show output of fr.readlines()
	print content1