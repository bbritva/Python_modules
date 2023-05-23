import pandas as pd
import sys

def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except Exception as exc:
            print(exc, file=sys.stderr)
            return None
    return wrapper

class FileLoader:
    @_guard_
    def load(self, path):
        """ takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame."""
        if not isinstance(path, str):
            raise ValueError("Error: wrong types of args")
        raw_data = pd.read_csv(path)
        print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
        return raw_data


    @_guard_
    def display(self, df, n):
        """takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive, or the last n rows if n is
        negative."""
        if not (isinstance(n, int) and isinstance(df, pd.DataFrame)):
            raise ValueError("Error: wrong types of args")
        if n != 0:
            print(df[:n] if (n > 0) else df[n:])

if __name__ == "__main__":
    fl = FileLoader()
    data = fl.load("../data/solar_system_census.csv")
    fl.display(data, 12)
    data = fl.load("../data/ssc_short.csv")
    fl.display(data, 12)
    print(type(data))
    print(isinstance(data, pd.DataFrame))
    print(isinstance(3, pd.DataFrame))
    print(isinstance("3", pd.DataFrame))