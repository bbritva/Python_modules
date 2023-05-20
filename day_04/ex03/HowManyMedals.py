from FileLoader import FileLoader

def how_many_medals(data, name):
    pass
    # data = data[(data["Year"] == year) & (data["Sex"] == gender)]
    # all_amount = data["Name"].unique().shape[0]
    # sport_amount = data[data["Sport"] == sport]["Name"].unique().shape[0]
    # return sport_amount / all_amount

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    print(how_many_medals(data, "Kjetil Andr Aamodt"))
    # Output
        # {1992: {’G’: 1, ’S’: 0, ’B’: 1},
        #  1994: {’G’: 0, ’S’: 2, ’B’: 1},
        #  1998: {’G’: 0, ’S’: 0, ’B’: 0},
        #  2002: {’G’: 2, ’S’: 0, ’B’: 0},
        #  2006: {’G’: 1, ’S’: 0, ’B’: 0}}