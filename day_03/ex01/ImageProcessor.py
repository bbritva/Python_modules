import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



class ImageProcessor:
    def load(self, path):
        try:
            img = Image.open(path)
            print(f"Loading image of dimensions {img.size[0]} x {img.size[1]}")
            return np.array(img)
        except FileNotFoundError:
            print("Exception: FileNotFoundError -- strerror: No such file or directory")
        except OSError:
            print("Exception: OSError -- strerror: None")

    def display(self, array):
        plt.imshow(array)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("non_existing_file.png")
    print(repr(arr))
    # Output :
    # None
    arr = imp.load("empty_file.png")
    # Output :
    # Exception: OSError -- strerror: None
    print(repr(arr))
    # Output :
    # None
    arr = imp.load("../resources/42AI.png")
    # Output :
    # Loading image of dimensions 200 x 200
    print(repr(arr))
    imp.display(arr)