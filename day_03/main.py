import numpy as np
from ex01.ImageProcessor import ImageProcessor
from ex03.ColorFilter import ColorFilter



if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("./resources/elon_canaGAN.png")
    # arr = imp.load("./resources/42AI.png")
    # Output :
    # Loading image of dimensions 200 x 200
    if not arr is None:
        cf = ColorFilter()
        inv_arr = cf.invert(arr)
        blue_arr = cf.to_blue(arr)
        red_arr = cf.to_red(arr)
        green_arr = cf.to_green(arr)
        cell_arr = cf.to_celluloid(arr)
        gs_arr = cf.to_grayscale(arr, "m")
        gsw_arr = cf.to_grayscale(arr, 'weight', weights = [0.8, 0.1, 0.1])

        imp.display(arr)
        imp.display(inv_arr)
        imp.display(blue_arr)
        imp.display(green_arr)
        imp.display(red_arr)
        imp.display(cell_arr)
        imp.display(gs_arr)
        imp.display(gsw_arr)
