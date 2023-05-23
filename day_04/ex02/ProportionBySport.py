from FileLoader import FileLoader
import pandas as pd

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
    print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
    # output is "0.01935"
    print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
    # output is "0.04127"
    print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
    # output is "0.00916"
