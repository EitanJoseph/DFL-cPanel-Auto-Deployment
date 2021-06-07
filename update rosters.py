import pandas as pd
import numpy as np
import json
import math

with open('players.json') as f:
  data = json.load(f)

df = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vTDyvnkgm1cYA0syoyqkkFVhJwmueNJ0JIAyO1lCjP2N7Md-zfC7ltU9DQvwWK0ud7DGY-lEPWMxERK/pub?gid=699917165&single=true&output=csv')


Team=["FC Coast", "Ship Maturity FC", "FC Ducklips", "Minotaurs FC", "Mofongo FC", "Golden Siors FC", "Rio FC", "Miners FC", "Lightning FC", "Atletico Yoink"]

allPlayers = set()
for t in Team:
	for p in data[t]["players"]:
		allPlayers.add(p["name"])

def playerExists(players, name):
	return name in players

for index, row in df.iterrows():
	j = 1
	while j < len(df.columns):
		if (type(row[j]) != str and math.isnan(row[j])):
			j+=2
			continue
		if playerExists(data[Team[int((j-1)/2)]]["players"], row[j]):
			continue
		data[Team[int((j-1)/2)]]["players"].append({
				"name":row[j],
				"number":index+1,
				"ga":[0,0],
				"town":row[j+1]
			})
		j+=2


with open("players.json", "w") as outfile: 
    json.dump(data, outfile)