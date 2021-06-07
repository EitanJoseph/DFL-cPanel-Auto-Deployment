function updateTeams(){

  const fs = require('fs')
  let rawdata = fs.readFileSync('schedule2019.json');
  let arr = JSON.parse(rawdata);

  for (var i = 0; i < arr.length; i++){
    var home = eval(arr[i].home);
    var away = eval(arr[i].away);
    home.gp += 1;
    away.gp += 1;
    
    if (arr[i].Hscore > arr[i].Ascore){
      home.won += 1;
      away.lost += 1;
      home.points += 3;
    }
    if (arr[i].Ascore > arr[i].Hscore){
      away.won += 1;
      home.lost += 1;
      away.points += 3;
    }
    if (arr[i].Hscore == arr[i].Ascore){
      home.points += 1;
      away.points += 1;
      home.drawn += 1;
      away.drawn += 1;
    }
    
    var goalDifferential = (arr[i].Hscore - arr[i].Ascore);
    home.gf += arr[i].Hscore;
    home.ga += arr[i].Ascore;
    home.gd += goalDifferential;
    away.gf += arr[i].Ascore;
    away.ga += arr[i].Hscore;
    away.gd -= goalDifferential;
  }
}

var FCC = {name: "FC Coast", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var SCD = {name: "SC Dwarchi", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
// Miners FC is named after Pickaxe FC as PFC
var PFC = {name: "Miners FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var RFC = {name: "Rio FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var GSFC = {name: "Golden Siors FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var SMFC = {name: "Ship Maturity FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var MFC = {name: "Minotaurs FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var LFC = {name: "Lightning FC", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};
var FCD = {name: "FC Deadlocs", gp: 0, won: 0, drawn: 0, lost: 0, gf: 0, ga:0, gd: 0, points: 0};

all_teams = [FCC, SCD, RFC, PFC, GSFC, SMFC, MFC, LFC, FCD]




function makeJSON(){
  updateTeams()
  const fs = require('fs')
  let rawdata = fs.readFileSync('players2019.json');
  let p = JSON.parse(rawdata);

  jsonObj = []
  for (i = 0; i < p.length; i++){
    if (i==1){i=2}
    teamObj = {
      name : all_teams[i].name,
      players : [],
      record : getRecord(i)
    }
    for (j = 0; j < p[i].length; j++){
      teamObj.players.push(p[i][j])
    }
    jsonObj.push(teamObj)
  }
  return jsonObj
}

function getRecord(i){
  return {
    gp : all_teams[i].gp,
    wins : all_teams[i].won,
    draws : all_teams[i].drawn,
    losses : all_teams[i].lost,
    gf : all_teams[i].gf,
    ga : all_teams[i].ga,
    gd : all_teams[i].gd,
    points : all_teams[i].points
  }
}

// ----- output to JSON object file ----

var dictstring = JSON.stringify(makeJSON());
var fs = require('fs');
fs.writeFile("stats2019.json", dictstring, function(err, result) {
     if(err) console.log('error', err);
   });
