from FileLoader import FileLoader

def how_many_medals(data, name):
    data = data[(data["Name"] == name) & (data["Medal"])]
    years = data["Year"].unique()
    result = {}
    for year in years:
        medals = data[data["Year"] == year]
        result[year] = {
            'G' : medals[medals["Medal"] == "Gold"].shape[0],
            'S' : medals[medals["Medal"] == "Silver"].shape[0],
            'B' : medals[medals["Medal"] == "Bronze"].shape[0],
        }
    return result

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    print(repr(how_many_medals(data, "Kjetil Andr Aamodt")))
    # Output
        # {1992: {’G’: 1, ’S’: 0, ’B’: 1},
        #  1994: {’G’: 0, ’S’: 2, ’B’: 1},
        #  1998: {’G’: 0, ’S’: 0, ’B’: 0},
        #  2002: {’G’: 2, ’S’: 0, ’B’: 0},
        #  2006: {’G’: 1, ’S’: 0, ’B’: 0}}