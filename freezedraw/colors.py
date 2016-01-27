import random
import matplotlib.pyplot as plt
import numpy as np
import colorsys
from freezedraw import image


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
    img = image.Image(w, h)
    for y in range(h):
        for x in range(w):
            img.set_pixel(x, y, bright_color_rgb())
    img.show()

    img2 = image.Image(w, h)
    for y in range(h):
        for x in range(w):
            img2.set_pixel(x, y, dark_color_rgb())
    img2.show()

    img3 = image.Image(w, h)
    c = bright_color_hsv()
    for y in range(h):
        for x in range(w):
            img3.set_pixel(x, y, colorsys.hsv_to_rgb(*near_hue_hsv(c)))
    img3.show()
