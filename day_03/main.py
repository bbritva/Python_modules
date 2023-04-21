import numpy as np
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter



if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("assets/42AI.png")
    # Output :
    # Loading image of dimensions 200 x 200
    cf = ColorFilter()
    cf.invert(arr)
    cf.to_green(arr)
    cf.to_red(arr)
    cf.to_blue(arr)
    cf.to_celluloid(arr)
    cf.to_grayscale(arr, 'm')
    cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5])