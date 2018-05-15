from PIL import Image
img = Image.open('logo.png').convert('LA')
img.save('logo_grayscale.png')