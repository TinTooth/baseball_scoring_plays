import statsapi

sched = statsapi.schedule(start_date="07/01/2018", end_date="07/31/2018", team=143)

divisions = statsapi.get("divisions", {"league": 104})
teams = statsapi.get("team", {'teamId':120})
national_league = statsapi.get('teams', {'leagueIds':104})
american_league = statsapi.get('teams', {'leagueIds':103})

scoring = statsapi.game_scoring_play_data(530769)



print(scoring)
