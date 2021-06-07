'''
This script 
	- Downloads the CSV file from the 2021 DFL master roster
	- Populates a new JSON object with empty player information
	- Exports the JSON object to "players.json"
'''

import pandas as pd
import numpy as np
import json
import math

df = pd.read_csv ('https://docs.google.com/spreadsheets/d/e/2PACX-1vTDyvnkgm1cYA0syoyqkkFVhJwmueNJ0JIAyO1lCjP2N7Md-zfC7ltU9DQvwWK0ud7DGY-lEPWMxERK/pub?gid=699917165&single=true&output=csv')

json_out = {}

Team=["FC Coast", "Ship Maturity FC", "FC Ducklips", "Minotaurs FC", "Mofongo FC", "Golden Siors FC", "Rio FC", "Miners FC", "Lightning FC", "Atletico Yoink"]

for i in range(0,len(Team)):
	json_out[Team[i]] = {
			"name":Team[i],
			"players":[]
		}

for index, row in df.iterrows():
	j = 1
	while j < len(df.columns):
		if (type(row[j]) != str and math.isnan(row[j])):
			j+=2
			continue
		json_out[Team[int((j-1)/2)]]["players"].append({
				"name":row[j],
				"number":index+1,
				"ga":[0,0],
				"town":row[j+1]
			})
		j+=2

with open("players.json", "w") as outfile: 
    json.dump(json_out, outfile)