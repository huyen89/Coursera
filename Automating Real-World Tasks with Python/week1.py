#!/usr/bin/python3

from PIL import Image
import os

path = 'images'
new_path = '/opt/icons'
filenames = os.listdir(path)

for file in filenames:
    try:
        img = Image.open(os.path.join(path, file))
        img = img.rotate(-90).resize((128, 128)).convert("RGB")
        img.save(os.path.join(new_path, file), format="JPEG")
        print("Writing new image:", os.path.join(new_path, file))
        img.close()
    except Exception as e:
        print("Skipping", os.path.join(path, file), "due to error:", str(e))
