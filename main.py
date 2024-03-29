import pathlib
import PIL
from PIL import Image

path = input('Full path of image: ')
image = PIL.Image.open(path)

USED_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

new_height = int(input('Image height: '))
new_width = int(new_height * image.width / image.height)

chara: str = ''.join(USED_CHARS[int(pixel // 25)] for pixel in
                     image.resize((int(new_width), int(new_height))).convert("L").getdata())

ascii_image = "\n".join([chara[index:(index + new_width)] for index in range(0, len(chara), new_width)])

print(ascii_image)

prefix = pathlib.PurePath(path).stem
with open(f"converted/ascii_{prefix}.txt", "w") as f:
    f.write(ascii_image)
