import os
import new_user_screen
import login_screen
import new_season_screen
import user
import home_screen
import update_team_screen
import select_user_screen
import change_season_screen
import game_screen
import pickle as pkl
import tkinter as tk
from tkinter import messagebox

class Launcher():
    """
    Primary handler for all pages. Contains the root, launches each page and holds persistent user data
    """
    
    def __init__(self):
        
        # Setup the root and load the initial login screen to begin
        self.root = tk.Tk()
        self.root.withdraw()
        self._window = login_screen.LoginScreen(master=self)
        self._current = self._window

        # Create a '/users' directory if one does not exist
        self.path=os.getcwd()
        os.listdir(self.path)
        if 'users' in os.listdir(self.path):
            pass
        else:
            os.mkdir(self.path+'/'+'users')
        self.user = None

    def launch_login(self,source=None, data=None):
        """
        Launches the login screen, destroys the launching page, and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = login_screen.LoginScreen(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_user_screen(self, source= None, data=None):
        """
        Launches the new user screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = new_user_screen.AddUserScreen(master=self,data=data)
        if source:
            source.destroy()
        self._current.focus_set()

    def launch_new_season(self,source=None,data=None):
        """
        Launches the new season screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = new_season_screen.AddSeasonScreen(master=self, data=data)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_home(self, source=None, data=None):
        """
        Launches the home screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = home_screen.HomeScreen(master=self,data=data)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_team(self,source=None,data=None):
        """
        Launches the update team screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = update_team_screen.TeamScreen(master=self,team=self.user.get_current_team())
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_choose_user(self,source=None):
        """
        Launches the choose user screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = select_user_screen.SelectUser(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_select_season(self,source=None):
        """
        Launches the select a season screen, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :data: Any needed data for initializing the page
        """
        self._current = change_season_screen.SelectSeason(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_play_game(self,source=None,quick_play=False):
        """
        Launches the play game screen, asks if the user is the home team, destroys the launching page and shifts focus
        :source: The currently displayed page, will destroy that page
        :quick_play: Boolean, False if launching from the login screen.
        """
        response = messagebox.askyesno("Choose side", "Are you playing the Home team?")
        if source:
            source.destroy()
        if response:
            self._current = game_screen.GameScreen(master=self, player='home',quickplay=quick_play)
        else:
            self._current = game_screen.GameScreen(master=self,player='away',quickplay=quick_play)
        self._current.focus_force()

    def change_season(self,season):
        """
        Changes the user active season
        :season: The season to change to
        """
        self.user.change_season(season)

    def new_user(self, name):
        """
        Generates a new user instance
        :name: the users name
        """
        self.user = user.User(name)

    def save_user(self):
        """
        Saves the user instance as a pkl file
        """
        filename=f'{self.user.get_name()}.pkl'
        path = os.getcwd()+"/users/"+filename
        with open(path, 'wb') as file:
            pkl.dump(self.user, file)

    def get_user(self,username):
        """
        Loads a user into memory
        :username: the name of the user to load
        """
        filename = f'{username}.pkl'
        path = os.getcwd() + "/users/" + filename
        with open(path, 'rb') as file:
            self.user = pkl.load(file)

# When called, startup the main loop for tkinter
if __name__ == '__main__':
    screens = []
    while True:
        if not screens:
            screen = Launcher()
            screens.append(screen)
            screen._window._window.mainloop()
