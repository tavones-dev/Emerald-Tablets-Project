from PIL import Image

# Open the PNG image
img = Image.open('throne_thoth.png')

# Convert to RGBA if not already
img = img.convert('RGBA')

# Create ICO file
img.save('throne_thoth.ico', format='ICO') 