'''
This script 
	- Downloads the CSV file from the 2021 DFL master schedule
	- Populates "players.json" JSON object with compiled player data
	- Populates "schedule.json" JSON object with compiled schedule data
	- Exports both JSON objects
'''

import pandas as pd
import numpy as np
import json
import math

with open('players.json') as f:
  players = json.load(f)

df = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vTDyvnkgm1cYA0syoyqkkFVhJwmueNJ0JIAyO1lCjP2N7Md-zfC7ltU9DQvwWK0ud7DGY-lEPWMxERK/pub?output=csv')

json_out = []

Team=["FC Coast", "Ship Maturity FC", "FC Ducklips", "Minotaurs FC", "Mofongo FC", "Golden Siors FC", "Rio FC", "Miners FC", "Lightning FC", "Atletico Yoink"]

def processPlayers(goals, assists, team):
	'''
	- processPlayers adds the goals and assists to the respective player objects
	'''
	goalsArr = goals.split(",") if type(goals) is str else []
	assistArr = assists.split(",") if type(assists) is str else []
	for i in goalsArr:
		players[team]["players"][int(i)-1]["ga"][0] += 1
	for i in assistArr:
		players[team]["players"][int(i)-1]["ga"][1] += 1

for i in range(0, df.shape[0]):
	if (math.isnan(df.loc[i, "Goals 1"]) or math.isnan(df.loc[i, "Goals 2"])):
		continue
	json_out.append({
			"date": df.loc[i, 'Date'],
			"home": df.loc[i, 'Team 1'],
			"Hscore": int(df.loc[i, 'Goals 1']),
			"away": df.loc[i, 'Team 2'],
			"Ascore": int(df.loc[i, 'Goals 2']),
			"field": df.loc[i, 'Field']
		})

	processPlayers(df.loc[i, "Team 1 Goal Scorers"], df.loc[i, "Team 1 Assists"], df.loc[i, "Team 1"])
	processPlayers(df.loc[i, "Team 2 Goal Scorers"], df.loc[i, "Team 2 Assists"], df.loc[i, "Team 2"])


with open("schedule.json", "w") as outfile: 
    json.dump(json_out, outfile)

with open("players.json", "w") as outfile: 
    json.dump(players, outfile)
