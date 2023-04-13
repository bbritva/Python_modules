from os.path import exists


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if filename is None:
            raise ValueError("filename is required")
        self.filename = filename
        if not exists(filename):
            raise ValueError("file does not exist")
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        data = []
        with open(self.filename, "r") as f:
            lines = f.readlines()
        for line in lines[self.skip_top:-self.skip_bottom]:
            curr_line = line.split(self.sep)
            data.append(curr_line)

        

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        pass


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
