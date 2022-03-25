import json

with open('players.json') as f:
  players = json.load(f)


table = f'<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script><table class=”searchable sortable”><thead><tr><th>Player</th><th>Goals</th><th>Assists</th><th>Town</th><th>Team</th></tr></thead><tbody>{"".join("<tr class=$item$><td>" + player["name"] +"</td>" + "<td>" + str(player["ga"][0]) +"</td>" + "<td>" + str(player["ga"][1]) +"</td>" + "<td>" + player["town"] +"</td>" + "<td>" + team +"</td></tr>" for team in players for player in players[team]["players"])}</tbody></table>'
table = table.replace("$", "\"")
with open('all_players.html', "w") as f:
    f.write(table)