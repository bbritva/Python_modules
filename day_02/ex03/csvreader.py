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
        self.file = open(self.filename, "r")
        if self.file is None:
            raise ValueError("file does not exist")
        self.lines = self.file.readlines()
        header = list(map(str.strip, self.lines[0].split(self.sep)))
        self.len = len(header)
        if self.header:
            self.header_value = header
            lines = self.lines[1:]
        else:
            lines = self.lines
        self.data = []
        
        for line in lines:
            curr_line = list(map(str.strip, line.split(self.sep)))
            if len(curr_line) != self.len:
                return None
            self.data.append(curr_line)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        begin = self.skip_top
        end = len(self.lines) - self.skip_bottom 
        return self.data[begin:end]

        
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is False:
            return None
        return self.header_value


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(header)
            print(data)
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(header)
            print(data)