import statsapi


class Players: 
    def __init__(self,players,player_teams):
        self.players = players
        self.teams = self.get_team_ids2(player_teams)

    # def get_plays ():
    #     pass 

    def get_team_ids2(self,player_teams):
        results = []
        all_teams = statsapi.get('teams', {'leagueIds':104})
        for team in player_teams:
            for ateam in all_teams['teams']:
                if team in ateam['name']:
                    results.append(ateam['id'])
        return results