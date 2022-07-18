import json

from numpy import hsplit
from sympy import Ge
K = 100
BASE = 800

with open('schedule.json') as f:
    schedule = json.load(f)

# dr = ELO_h - ELO_a
# E = 1/(1+10^(-dr/400))
# ELO_h_n = ELO_h + KG(O-E)
# O in {0, 0.5, 1}
# K = 100
# Base = 800
# G = 1 if MOV = 0, 1, 1.5 if MOV = 2, else (11+MOV)/8
def ELO_function(t1, t2, game):
  dr = t1[6] - t2[6]
  E = 1/(1+10**(-dr/400))
  O = 1 if game['Hscore'] > game['Ascore'] else 0.5 if game['Hscore'] == game['Ascore'] else 0
  MOV = abs(game['Hscore'] - game['Ascore'])
  G = 1 if MOV <= 1 else 1.5 if MOV == 2 else (11+MOV)/8
  diff = round(K*G*(O-E))
  t1[6] += diff
  t2[6] -= diff



def new_team():
  return [0]*6 + [BASE]

def update_team(team, opp, game, home=True):
  team[0] += 1
  team[1] += game['Hscore'] > game['Ascore'] if home else game['Hscore'] < game['Ascore']
  team[2] += game['Hscore'] == game['Ascore']
  team[3] += game['Hscore'] < game['Ascore'] if home else game['Hscore'] > game['Ascore']
  team[4] += game['Hscore'] if home else game['Ascore']
  team[5] += game['Hscore'] if not home else game['Ascore']
  home = False
  opp[0] += 1
  opp[1] += game['Hscore'] > game['Ascore'] if home else game['Hscore'] < game['Ascore']
  opp[2] += game['Hscore'] == game['Ascore']
  opp[3] += game['Hscore'] < game['Ascore'] if home else game['Hscore'] > game['Ascore']
  opp[4] += game['Hscore'] if home else game['Ascore']
  opp[5] += game['Hscore'] if not home else game['Ascore']
  ELO_function(team, opp, game)
  
teams = {}
for game in schedule:
  if game['home'] not in teams:
    teams[game['home']] = new_team()
  if game['away'] not in teams:
    teams[game['away']] = new_team()
  update_team(teams[game['home']], teams[game['away']], game, False)



def row(name, team, i):
  return "<tr class=$item$><td>" + str(i) +"</td>" + "<td>" + name +"</td>" + "<td>" + str(team[0]) +"</td>" + "<td>" + str(team[1]) + " - " + str(team[2]) + " - " + str(team[3]) +"</td>" + "<td>" + str(team[4]) +"</td>" + "<td>" + str(team[5]) +"</td>" + "<td>" + str(team[4] - team[5])  +"</td>" + "<td>" + str(team[6])  +"</td>" + "</tr>"

table = f'<table><thead><tr><th>Pos</th><th>Team</th><th>GP</th><th>W - T - L</th><th>GF</th><th>GA</th><th>GD</th><th>ELO</th></tr></thead><tbody>{"".join(row(team[0], team[1], i+1) for i,team in enumerate(sorted(teams.items(), reverse=True,key=lambda x: x[1][6])))}</tbody></table>'
table = table.replace("$", "\"")
with open('ELO_table.html', "w") as f:
  f.write(table)

