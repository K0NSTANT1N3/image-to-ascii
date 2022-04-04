import PIL.Image

path = 'images/violin-girl.jpg'
image = PIL.Image.open(path)

USED_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
new_width = 150

chara: str = ''.join(USED_CHARS[pixel // 25] for pixel in
                     image.resize((int(new_width), int(new_width * image.height / image.width))).convert("L").getdata())

ascii_image = "\n".join([chara[index:(index + new_width)] for index in range(0, len(chara), new_width)])

print(ascii_image)
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)

