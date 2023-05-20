from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
        pass
    
    def when(self, location):
        """takes a location as an argument and returns a list containing the
        years where games were held in the given location,"""
        return self.data[self.data["City"] == location]["Year"].unique().tolist()

    def where(self, date):
        """takes a date as an argument and returns the location where the
        Olympics took place in the given year."""
        return self.data[self.data["Year"] == date]["City"].unique()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    # Output
    # [’Athina’]
    print(sp.where(2016))
    # Output
    # [’Rio de Janeiro’]
    print(sp.when('Athina'))
    # Output
    # [2004, 1906, 1896]
    print(sp.when('Paris'))
    # Output
    # [1900, 1924]