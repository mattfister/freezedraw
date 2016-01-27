import numpy as np
import matplotlib.pyplot as plt


class Image(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = np.ones((h, w, 3))

    def set_pixel(self, x, y, rgb):
        self.data[y][x] = rgb

    def show(self):
        plt.imshow(self.data, interpolation='nearest')
        plt.show()

