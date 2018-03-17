## 2. Introduction to the Data ##

import csv

years = dict()

# read in csv to list of lists 'nfl_suspensions'
f = open("nfl_suspensions_data.csv", 'r')
nfl_suspensions_data = csv.reader(f)
nfl_suspensions = list(nfl_suspensions_data)
# remove header row
nfl_suspensions = nfl_suspensions[1:]

# get sum of suspensions per year
for suspension in nfl_suspensions:
    row_year = suspension[5]
    count = years.get(row_year, 0)
    years[row_year] = count + 1
    
print(years)

## 3. Unique Values ##

import csv

f = open("nfl_suspensions_data.csv", 'r')
suspensions_data = csv.reader(f)
suspensions = list(suspensions_data)[1:]

# per instructions, we use two list comprehensions
teams = [suspension[1] for suspension in suspensions]
unique_teams = set(teams)

games = [suspension[2] for suspension in suspensions]
unique_games = set(games)

print(unique_teams)
print(unique_games)

## 4. Suspension Class ##

import csv

class Suspension():
    def __init__(self, row):
        self.name  = row[0]
        self.team  = row[1]
        self.games = row[2]
        self.year  = row[5]

third_suspension = Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name  = row[0]
        self.team  = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    
    def get_year(self):
        return self.year
    
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()