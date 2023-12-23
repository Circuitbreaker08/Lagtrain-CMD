import os
import time
import json
from pygame import mixer

with open("data.json") as f:
    data = json.loads(f.read())
os.system("color 80")
os.system("title Lagtrain")
mixer.init()
mixer.music.load("lagtrain.ogg")
mixer.music.play()
start = time.time()
for frame in range(len(data)):
    print("\r", data[frame], end="\r")
    time.sleep(
        max(
            0,
            (frame * (1/15) + start) - time.time()
        )
    )

print(start - time.time())