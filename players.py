import statsapi


class Players: 
    def __init__(self,players,player_teams):
        self.players = players
        self.teams = self.get_team_ids(player_teams)

    def get_plays (self):
        games = []
        for team in self.teams:
            new_games = statsapi.schedule(start_date="07/01/2018", end_date="07/31/2018", team=team)
            for g in new_games:
                games.append(g)
        return games

    def get_team_ids(self,player_teams):
        results = []
        all_teams = statsapi.get('teams', {'leagueIds':104})
        for team in player_teams:
            for ateam in all_teams['teams']:
                if team in ateam['name']:
                    results.append(ateam['id'])
        return results