import user
import time

class User:
    def __init__(self, name):
        self._name = name
        self._seasons = {}
        self._current_team = [None for i in range(15)]
        self._current_season = None

    def add_season(self,season_name,team=None, num_of_games=33):

        if team == None:
            team=[None for i in range(15)]
        self._seasons[season_name]={'team':team,
                                           'num_of_games':num_of_games,
                                            'games':[]
                                           }
        self._current_season=season_name
        self._current_team = team

    def get_name(self):
        return self._name
    def get_current_team(self):
        return self._current_team

    def get_seasons(self):
        return list(self._seasons.keys())

    def get_team(self):
        return self._current_team

    def get_current_season(self):
        return self._current_season

    def update_team(self, new_team):
        self._current_team=new_team
        self._seasons[self._current_season]['team'] = new_team

    def change_season(self,new_season):
        self._current_season = new_season
        self._current_team = self._seasons[new_season]['team']

    def add_game_to_season(self,outcome):
        self._seasons[self._current_season]['games'].append(outcome)

    def get_win_loss(self):
        season = self._seasons[self._current_season]['games']
        wins= 0
        losses = 0
        games = self._seasons[self._current_season]['num_of_games']
        for i in range(len(season)):
            if season[i] == 'w':
                wins+=1
            elif season[i]=='l':
                losses += 1
        return (wins,losses,games)


