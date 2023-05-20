from FileLoader import FileLoader

def proportion_by_sport(data, year, sport, gender):
    data = data[(data["Year"] == year) & (data["Sex"] == gender)]
    all_amount = data["Name"].unique().shape[0]
    sport_amount = data[data["Sport"] == sport]["Name"].unique().shape[0]
    return sport_amount / all_amount

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    # Output
    # Loading dataset of dimensions 271116 x 15
    print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
    # Output
    # 0.019302325581395347