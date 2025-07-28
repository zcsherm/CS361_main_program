import os#

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
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self._window = login_screen.LoginScreen(master=self)
        self._current = self._window
        self.path=os.getcwd()
        os.listdir(self.path)
        if 'users' in os.listdir(self.path):
            pass
        else:
            os.mkdir(self.path+'/'+'users')
        self.user = None

    def launch_login(self,source=None, data=None):
        self._current = login_screen.LoginScreen(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_user_screen(self, source= None, data=None):
        self._current = new_user_screen.AddUserScreen(master=self,data=data)
        if source:
            source.destroy()
        self._current.focus_set()

    def launch_new_season(self,source=None,data=None):
        self._current = new_season_screen.AddSeasonScreen(master=self, data=data)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_home(self, source=None, data=None):
        self._current = home_screen.HomeScreen(master=self,data=data)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_team(self,source=None,data=None):
        self._current = update_team_screen.TeamScreen(master=self,team=self.user.get_current_team())
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_choose_user(self,source=None):
        self._current = select_user_screen.SelectUser(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_select_season(self,source=None):
        self._current = change_season_screen.SelectSeason(master=self)
        if source:
            source.destroy()
        self._current.focus_force()

    def launch_play_game(self,source=None,quick_play=False):
        response = messagebox.askyesno("Choose side", "Are you playing the Home team?")
        if source:
            source.destroy()
        if response:
            self._current = game_screen.GameScreen(master=self, player='home',quickplay=quick_play)
        else:
            self._current = game_screen.GameScreen(master=self,player='away',quickplay=quick_play)
        self._current.focus_force()

    def change_season(self,season):
        self.user.change_season(season)

    def new_user(self, name):
        self.user = user.User(name)

    def save_user(self):
        filename=f'{self.user.get_name()}.pkl'
        path = os.getcwd()+"/users/"+filename
        with open(path, 'wb') as file:
            pkl.dump(self.user, file)

    def get_user(self,username):
        filename = f'{username}.pkl'
        path = os.getcwd() + "/users/" + filename
        with open(path, 'rb') as file:
            self.user = pkl.load(file)

if __name__ == '__main__':
    screens = []
    while True:
        if not screens:
            screen = Launcher()
            screens.append(screen)
            screen._window._window.mainloop()