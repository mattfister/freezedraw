import random
import matplotlib.pyplot as plt
import numpy as np
import colorsys


def bright_color_hsv():
    hsv = (random.uniform(0.0, 1.0), random.uniform(0.9, 1.0), random.uniform(0.9, 1.0))
    return hsv


def dark_color_hsv():
    hsv = (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 0.5))
    return hsv


def near_hue_hsv(hsv):
    h = hsv[0]+random.uniform(-0.1, 0.1)
    if h < 0.0:
        h = 1.0 + h
    hsv2 = (h, hsv[1], hsv[2])
    return hsv2


def bright_color_rgb():
    rgb = colorsys.hsv_to_rgb(*bright_color_hsv())
    return rgb


def dark_color_rgb():
    rgb = colorsys.hsv_to_rgb(*dark_color_hsv())
    return rgb


if __name__=='__main__':
    h = 100
    w = 100
    img = np.ones((w, h, 3))
    for y in range(h):
        for x in range(w):
            img[x][y] = bright_color_rgb()
    plt.imshow(img, interpolation='nearest')
    plt.show()
    img2 = np.ones((w, h, 3))
    for y in range(h):
        for x in range(w):
            img2[x][y] = dark_color_rgb()
    plt.imshow(img2, interpolation='nearest')
    plt.show()
    img3 = np.ones((w, h, 3))
    c = bright_color_hsv()
    for y in range(h):
        for x in range(w):
            img3[x][y] = colorsys.hsv_to_rgb(*near_hue_hsv(c))
    plt.imshow(img3, interpolation='nearest')
    plt.show()
