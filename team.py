class Team:
    def __init__(self, data):
        self._name = data["name"]
        self._roster = data["roster"]
        self._season_wins = data["season wins"]
        self._season_losses = data["season losses"]
        self._overall_wins = data["overall wins"]
        self._overall_losses = data["overall losses"]

    def update_name(self, name):
        self._name = name

    def update_team(self, new_team):
        self._roster = new_team

    def update_season_wins(self, number):
        self._season_wins = number

    def increment_season_wins(self):
        self._season_wins += 1

    def decrement_season_wins(self):
        self._season_wins -= 1

    def update_season_losses(self, number):
        self._season_losses = number

    def increment_season_losses(self):
        self._season_losses += 1

    def decrement_season_losses(self):
        self._season_losses -= 1

    def update_overall_wins(self, number):
        self._overall_wins = number

    def increment_overall_wins(self):
        self._overall_wins += 1

    def decrement_overall_wins(self):
        self._overall_wins -= 1

    def update_overall_losses(self, number):
        self._overall_losses = number

    def increment_overall_losses(self):
        self._overall_losses += 1

    def decrement_overall_losses(self):
        self._overall_losses -= 1

    def get_season_wins(self):
        return self._season_wins

    def get_season_losses(self):
        return self._season_losses

    def get_overall_wins(self):
        return self._overall_wins

    def get_overall_losses(self):
        return self._overall_losses

    def get_roster(self):
        return self._roster

    def get_name(self):
        return self._name

    def get_contents(self):
        return {
            "name": self._name,
            "roster": self._roster,
            "season wins": self._season_wins,
            "season losses": self._season_losses,
            "overall wins": self._overall_wins,
            "overall losses": self._overall_losses
        }
