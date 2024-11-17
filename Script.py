import os
from PIL import Image
import keyboard
import time

def is_close_to_white(rgb_t):
    p = 220
    r, g, b = rgb_t
    if r > p and g > p and b > p:
        return True
    return False


im = Image.open('Trollface.jpg')
print(os.stat('Trollface.jpg').st_size)
imageSizeW, imageSizeH = im.size
print(imageSizeW, imageSizeH)
blackWhitePixels = {}

for y in range(0, imageSizeH):
    for x in range(0, imageSizeW):
        pixVal = im.getpixel((x, y))
        if pixVal == (255, 255, 255):
            blackWhitePixels[(x, y)] = (255 << 16 | 255 << 8 | 255)
            im.putpixel((x, y), (255, 255, 255))
        elif pixVal != (255, 255, 255) and is_close_to_white(pixVal):
            blackWhitePixels[(x, y)] = (255 << 16 | 255 << 8 | 255)
            im.putpixel((x, y), (255, 255, 255))
        else:
            blackWhitePixels[(x, y)] = (0 << 16 | 0 << 8 | 0)
            im.putpixel((x, y), (0, 0, 0))

print(bin(230 << 16 | 0 << 8 | 0))

im.save("black_white_trollface.png", format="PNG")
im.show()

print(len(blackWhitePixels))

with open('pixels.txt', 'w') as file:
    for i, row in enumerate(blackWhitePixels):
        xy = tuple(row)
        file.write(f"{i}: {xy},{blackWhitePixels[row]}\n")

black_pixels_coords = [pixel for pixel in blackWhitePixels if blackWhitePixels[pixel] == 0]

with open('black_pixels.txt', 'w') as file:
    for coord in black_pixels_coords:
        file.write(f"{coord}\n")

keys_iter = iter(blackWhitePixels.keys())

while not keyboard.is_pressed('q'):
    key = keyboard.read_key()
    if key == 'a':
        coords = next(keys_iter)
        if blackWhitePixels[coords] == 16777215:
            print(coords, 'white')
        else:
            print(coords, 'black')
        time.sleep(0.2)



