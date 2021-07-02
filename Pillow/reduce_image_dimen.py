from PIL import Image as img
import math

# Opening the image
image = img.open('./img/scene.jpg')

wd, ht = image.size  # Size of image
print(wd, ht)

# New size of image
new_wd = 720
# This calculation is done to maintain aspect ratio
new_ht = math.floor((ht / wd) * new_wd)

# Resizing the image
image1 = image.resize((new_wd, new_ht))
print(image1.size)

# Saving the image
image1.save('./img/scene_resized.jpg')

# Converting the image to black and white
image2 = image.convert('1')
image2.save('./img/scene_bnw.jpg')
