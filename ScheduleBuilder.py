import json

with open('schedule.json') as f:
    schedule = json.load(f)

schedule.reverse()

def row(game):
  return "<tr class=$item$><td>" + game["date"] +"</td>" + "<td>" + game["home"] +"</td>" + "<td>" + str(game["Hscore"]) + " - " + str(game["Ascore"]) +"</td>" + "<td>" + game["away"] +"</td>" + "<td>" + game["field"] +"</td>" + "</tr>"

table = f'<table><thead><tr><th>Date</th><th>Home</th><th>Score</th><th>Away</th><th>Field</th></tr></thead><tbody>{"".join(row(game) for game in schedule)}</tbody></table>'
table = table.replace("$", "\"")
with open('schedule.html', "w") as f:
  f.write(table)
