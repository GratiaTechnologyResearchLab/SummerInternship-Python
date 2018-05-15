import os

srcFileName = raw_input("Enter source filename:")
destFileName = raw_input("Enter destination filename:")

# Convert source file to destination file
os.system('convert ' + srcFileName + ' ' + destFileName)

from PIL import Image

# To convert RGB image to Grayscale image
img = Image.open(destFileName).convert('LA')
img.save("Grayscale" + destFileName)