import json

from numpy import hsplit

with open('schedule.json') as f:
    schedule = json.load(f)

def new_team():
  return [0]*6

def update_team(team, game, home=True):
  team[0] += 1
  team[1] += game['Hscore'] > game['Ascore'] if home else game['Hscore'] < game['Ascore']
  team[2] += game['Hscore'] == game['Ascore']
  team[3] += game['Hscore'] < game['Ascore'] if home else game['Hscore'] > game['Ascore']
  team[4] += game['Hscore'] if home else game['Ascore']
  team[5] += game['Hscore'] if not home else game['Ascore']

teams = {}
for game in schedule:
  if game['home'] not in teams:
    teams[game['home']] = new_team()
  update_team(teams[game['home']], game)
  if game['away'] not in teams:
    teams[game['away']] = new_team()
  update_team(teams[game['away']], game, False)



def row(name, team, i):
  return "<tr class=$item$><td>" + str(i) +"</td>" + "<td>" + name +"</td>" + "<td>" + str(team[0]) +"</td>" + "<td>" + str(team[1]) + " - " + str(team[2]) + " - " + str(team[3]) +"</td>" + "<td>" + str(team[4]) +"</td>" + "<td>" + str(team[5]) +"</td>" + "<td>" + str(team[4] - team[5])  +"</td>" + "<td>" + str(team[1]*3 + team[2])  +"</td>" + "</tr>"

table = f'<table><thead><tr><th>Pos</th><th>Team</th><th>GP</th><th>W - T - L</th><th>GF</th><th>GA</th><th>GD</th><th>Points</th></tr></thead><tbody>{"".join(row(team[0], team[1], i+1) for i,team in enumerate(sorted(teams.items(), reverse=True,key=lambda x: x[1][1]*3 + x[1][2])))}</tbody></table>'
table = table.replace("$", "\"")
with open('table.html', "w") as f:
  f.write(table)

