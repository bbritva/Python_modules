from FileLoader import FileLoader
import pandas as pd


def how_many_medals_by_country(data, country):
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

    data = data[(data["Team"] == country) & (data["Medal"])][['Team', 'Year', 'Sport', 'Medal']]
    team_medals = data[data["Sport"].isin(team_sports)].drop_duplicates()
    ind_medals = data[~data["Sport"].isin(team_sports)]
    data = pd.concat([team_medals, ind_medals])
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

    print(how_many_medals_by_country(data, 'Test_team'))
    # Output
    # {2192: {’G’: 17, ’S’: 14, ’B’: 23}, 2196: {’G’: 8, ’S’: 21, ’B’: 19}, 2200: {’G’: 26, ’S’: 19, ’B’: 7}}
