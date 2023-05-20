from FileLoader import FileLoader

def proportion_by_sport(data, year, sport, gender):
    data = data[[data["Year"] == year, data["Sex"] == gender]]
    print("{'f':", female_age,", 'm':", male_age, "}")

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    # Output
    # Loading dataset of dimensions 271116 x 15
    youngest_fellah(data, 2004)
    # Output
    # {’f’: 13.0, ’m’: 14.0}