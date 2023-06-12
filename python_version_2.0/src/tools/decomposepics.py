import os
from PIL import Image
from PIL import ImageSequence


def decomposePics(original_image_path, saved_image_path):
    i = 0
    img = Image.open(original_image_path)
    folder = saved_image_path
    if not os.path.isdir(folder):
        os.mkdir(saved_image_path)
    for frame in ImageSequence.Iterator(img):
        frame.save(os.path.join(saved_image_path, "frame{}.png".format(i+1)))
        i += 1