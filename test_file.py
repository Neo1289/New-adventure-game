import os
from PIL import Image

####### FUNCTION USED TO TEST COLORS WITH IMAGES#######
img_path = os.path.join("resources", "torch", "1.png")
img = Image.open(img_path).convert("RGB")  # converts to RGB mode, no alpha channel

pixel_value = img.getpixel((10, 10))
print("Sampled pixel:", pixel_value)  # prints a 3-value tuple for RGB