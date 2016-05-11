from PIL import Image
import glob
import os
base_dir = os.path.join(os.getcwd(), "GTM")
img_collection = glob.glob(base_dir + '\\' + '*.jpg')
img_number = len(img_collection)
raw_img_1 = Image.open(img_collection[1])
# raw_img_1.show()
mode = raw_img_1.mode
size = raw_img_1.size
height = int(img_number / 15)
width = 15
meta_size = [0, 0]
meta_size[0] = size[0] * height
meta_size[1] = size[1] * width
meta_img = Image.new(mode=mode, size=meta_size)
for i in range(width):
    for j in range(height):
        box = (j * size[0], i * size[1])
        raw_img = Image.open(img_collection[j * width + i])
        meta_img.paste(raw_img, box=box)
meta_img.show()
meta_img.save('meta_img.jpg')
