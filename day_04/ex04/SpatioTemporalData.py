from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
        pass
    
    def when(self, location):
        """takes a location as an argument and returns a list containing the
        years where games were held in the given location,"""
        pass

    def where(self, date):
        """takes a date as an argument and returns the location where the
        Olympics took place in the given year."""
        pass

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    sp = SpatioTemporalData(data)
    sp.where(1896)
    # Output
    # [’Athina’]
    sp.where(2016)
    # Output
    # [’Rio de Janeiro’]
    sp.when('Athina')
    # Output
    # [2004, 1906, 1896]
    sp.when('Paris')
    # Output
    # [1900, 1924]