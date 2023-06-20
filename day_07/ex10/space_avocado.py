import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pickle 


if __name__ == "__main__":

    with open("model.pickle", 'rb') as my_file:
        print(pickle.load(my_file))
