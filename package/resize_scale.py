# -*- coding: utf-8 -*-
# resize
from PIL import Image
import glob


def resize(copy_path):
    path = copy_path + '/*'
    files = glob.glob(path)
    img_height = int(input('幅: '))
    img_width = int(input('高さ: '))

    for file in files:
        img = Image.open(file)
        img_resized = img.resize((img_height, img_width))
        img_resized.save(file)
    max_len = max(img_height, img_width)
    return max_len
