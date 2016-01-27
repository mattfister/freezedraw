import random
import matplotlib.pyplot as plt
import numpy as np
import colorsys

def bright_color_hsv():
    hsv = (random.uniform(0.0, 1.0), random.uniform(0.9, 1.0), random.uniform(0.9, 1.0))
    return hsv

def bright_color_rgb():
    rgb = colorsys.hsv_to_rgb(*bright_color_hsv())
    rgb2 = [c * 255 for c in rgb]
    print(rgb2)
    return rgb2


if __name__=='__main__':
    h = 880
    w = 440
    img = np.ones((w, h, 3))*bright_color_rgb()
    for x in range(440):
        for y in range(880):
            img[x][y] = bright_color_rgb()
    plt.imshow(img)
    plt.show()