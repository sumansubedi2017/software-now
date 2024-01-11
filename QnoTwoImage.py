from PIL import Image
import numpy as np
import time
#Open the original picture.
original_image_path = 'chapter1.jpg'
original_image = Image.open(original_image_path)

#Obtain the image  dimensions.
width, height = original_image.size

#Make a number using the provided algorithm
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

#Take the changed pixels and make a new picture.
new_image = Image.new('RGB', (width, height))

#Loop over a each pixel and apply the conversion.
for x in range(width):
    for y in range(height):
        original_pixel = original_image.getpixel((x, y))
        converted_pixel = tuple(val + generated_number for val in original_pixel)
        new_image.putpixel((x, y), converted_pixel)

#Save the updated picture.
new_image_path = 'chapter1out.png'
new_image.save(new_image_path)

#Find the total red pixel values in the new image.
red_sum = np.sum(np.array(new_image)[:, :, 0])

#display the sum of red pixel
print("Sum of red pixel values in the new image:", red_sum)

#GitHub repository https://github.com/sumansubedi2017/software-now.git