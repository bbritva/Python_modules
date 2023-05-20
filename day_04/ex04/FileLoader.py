import pandas as pd

def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print(e) 
            return None
    return wrapper

class FileLoader:
    @_guard_
    def load(self, path):
        """ takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame."""
        raw_data = pd.read_csv(path)
        print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
        return raw_data


    @_guard_
    def display(self, df, n):
        """takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive, or the last n rows if n is
        negative."""
        print(df[:n])
        rows = df.shape[0] if df.shape[0] < n else n
        print("[", rows, "rows x", df.shape[1], "columns]")

