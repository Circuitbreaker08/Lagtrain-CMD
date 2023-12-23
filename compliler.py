import os
import cv2
import json
from PIL import Image

data = []
video = cv2.VideoCapture("lagtrain.mp4")

counter = 0
white = False
while counter <+ 3777:
    line = ""
    im = Image.fromarray(video.read()[1]).resize((256, 144)) #font size 8 -> (256, 144); default cmd is 16 pts
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            color = im.getpixel((x, y))[0]
            if color >= 170 and color <= 200:
                line += " "
            else:
                pass
                if color <= 60:
                    if white:
                        line += "\033[30m"
                        white = False
                elif color >= 200:
                    if not white:
                        line += "\033[37m"
                        white = True
                line += "%"
        line += "\n"
    data.append(line)
    counter += 1
    print("\r", counter, end="")

with open("data.json", "w") as f:
    f.write(json.dumps(data, indent=1))