import statsapi
from datetime import date


class Plays: 
    def __init__(self,players,player_teams):
        self.players = players
        self.teams = self.get_team_ids(player_teams)
        self.games = self.get_games()

    def get_games (self):
        games = []
        for team in self.teams:
            new_games = statsapi.schedule(start_date="07/01/2022", end_date="07/31/2022", team=team)
            # new_games = statsapi.schedule(start_date=date.today, end_date=date.today, team=team)
            for g in new_games:
                games.append(g['game_id'])
        return games
        

    def get_team_ids(self,player_teams):
        results = []
        nl_teams = statsapi.get('teams', {'leagueIds':104})
        al_teams = statsapi.get('teams', {'leagueIds':103})
        for team in player_teams:
            for ateam in nl_teams['teams']:
                if team in ateam['name']:
                    results.append(ateam['id'])
            for ateam in al_teams['teams']:
                if team in ateam['name']:
                    results.append(ateam['id'])
        
        return results

    def get_plays(self):
        results = []
        game_plays = []
        for game in self.games:
            game_plays.append(statsapi.game_scoring_play_data(game))
        for game in game_plays:
            for play in game['plays']:
                for player in self.players:
                    if player in play['result']['description']:
                        results.append(play['result']['description'])
        return results