from PIL import Image
import numpy as np
import sys
import math

# Make sure the args are passed 
if len(sys.argv) != 3:
    print("Invalid Arguments, please pass [filename.bin] and [output.png]!")
    exit(1)
else:
    print("Tring to open \'", sys.argv[1], "\'!")

# make a file object
f = open(sys.argv[1], "rb")

# Convert the file object to an array
ByteArray = list(f.read())

# Make some temp arrays for constructing the main pixel array
ColorArray = []
pixels = []

# Constrct pixel map
print("Constructing pixel map")
for i in ByteArray:
    # Make a cool color
    Red     = math.tan(i) * 255
    Green   = math.cos(i) * 255
    Blue    = math.sin(i) * 255

    # Make NULL black
    if Green == 255 and Blue == 0 and Red == 0:
        Green = 0

    # Construct the color
    Color = (Red, Green, Blue)
    
    # Add the color to the array
    ColorArray.append(Color)
    if len(ColorArray) >= 1000:
        pixels.append(ColorArray)
        ColorArray = []

# Clean up old arrays
ByteArray = []
ColorArray = []

# Tell the user the image size
print(len(pixels[0]), "x", len(pixels), " Constructed!")

# Convert to pixels to a 'np array'
print("Converting Array type")
array = np.array(pixels, dtype=np.uint8)

# Clean up the old array
pixels = []

# Construct the image
print("Constructing Image from Array")
new_image = Image.fromarray(array)

# Save the final product 
print("Saving Image")
new_image.save(sys.argv[2])
print("done!")
