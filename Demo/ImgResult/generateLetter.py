from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

# Set the image size and font size
image_size = (100, 100)
font_size = 80

# Create a blank image with white background in grayscale mode
image = Image.new('L', image_size, 255)
draw = ImageDraw.Draw(image)

font_path = "C:/Windows/Froints/BRITANIC.TTF"
font = ImageFont.truetype(font_path, font_size)

class_names = ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'
         'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
         'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r'
         's' 't' 'u' 'v' 'w' 'x' 'y' 'z']

class_names = class_names[0]

# Iterate over A-Z and generate the images
for i in range(62):
    # Clear the image for each iteration
    draw.rectangle([(0, 0), image_size], fill=255)

    # Calculate the position to center the letter
    letter = class_names[i]
    letter_width, letter_height = draw.textsize(letter, font=font)
    x = (image_size[0] - letter_width) // 2
    y = (image_size[1] - letter_height) // 2

    # Draw the letter on the image
    draw.text((x, y), letter, fill=0, font=font)

    if (i < 36):
        image_path = f"{letter}.png"
    else:
        image_path = f"{letter}_lower.png"
    if os.path.exists(image_path):
        os.remove(image_path)

    # Save the image
    image.save(image_path)

# Create a white image 
image = Image.new('L', image_size, 255)
image.save("empty.png")