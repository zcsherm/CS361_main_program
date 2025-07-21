class Inning:
    def __init__(self):
        self._away = 0
        self._home = 0

    def set_away(self, score):
        self._away = score

    def increment_away(self):
        self._away += 1

    def set_home(self, score):
        self._home = score

    def increment_home(self):
        self._home += 1

    def get_scores(self):
        return (self._away, self._home)

    def get_away_score(self):
        return self._away

    def get_home_score(self):
        return self._home

    def decrement_away(self):
        self._away -= 1

    def decrement_home(self):
        self._home -= 1

class FullGame:
    def __init__(self):
        self._innings = [Inning() for i in range(6)]

    def add_inning(self):
        self._innings.append(Inning())

    def get_home_score(self):
        home = 0
        for inning in self._innings:
            home += inning.get_home_score()
        return home

    def get_away_score(self):
        away = 0
        for inning in self._innings:
            away += inning.get_away_score()
        return away
    
    def get_inning_home(self, inning):
        return self._inning[inning-1].get_home_score()

    def get_inning_away(self, inning):
        return self._inning[inning-1].get_away_score()
        
    def update_inning_home(self, inning, score):
        inning_home = self._inning[inning-1]
        inning_home.set_home(score)
        
    def update_inning_away(self, inning, score):
        inning_away = self._inning[inning-1]
        inning_away.set_away(score)

    def increment_inning_home(self, inning):
        self._inning[inning-1].increment_home()

    def increment_inning_away(self, inning):
        self._inning[inning-1].increment_away()

    def decrement_inning_home(self, inning):
        self._inning[inning-1].decrement_home()

    def decrement_inning_away(self, inning):
        self._inning[inning-1].decrement_away()
        
class BoxScore:
    
    def __init__(self):
        self._game = FullGame()
        self._current_inning = 1
        self._number_of_innings = 6

    def get_current_score(self):
        home = self._game.get_home_score()
        away = self._game.get_away_score()
        return (away, home)

    def get_inning_scores(self,inning):
        away = self._game.get_inning_home(inning)
        home = self._game.get_inning_away(inning)
        return (away, home)
        
    def check_winner(self):
        away, home = self.get_current_score()
        if away > home:
            return "away"
        if home > away:
            return "home"
        return "tie"

    def add_extra_innings(self):
        self._game.add_inning()

    def set_visitor(self, inning,score):
        self._game.update_inning_away(score)

    def set_home(self, inning,score):
        self._game.update_inning_home(score)

    def increment_visitor(self, inning):
        self._game.increment_inning_away()

    def increment_visitor(self, inning):
        self._game.increment_inning_home()

    def decrement_visitor(self, inning):
        self._game.decrement_inning_away()

    def decrement_visitor(self, inning):
        self._game.decrement_inning_home()
