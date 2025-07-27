from tkinter import messagebox, ttk
import tkinter as tk
import os

# Add frames for spacing the buttons
# Add proper window geometry

class LoginScreen(tk.Toplevel):
    def __init__(self, master):
        #self._window = tk.Tk()
        #self._window.config(width=600, height=600)
        #self._window.title("Welcome")
        super().__init__()
        self._window= self
        self.title=("welcome")
        self._master = master
        txt1 = "Welcome to the tracker for Baseball Highlights: 2045!"
        label = tk.Label(self._window, text=txt1)
        label.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)
        label = tk.Label(self._window, text = 'Please make a selection below')
        label.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)
        self._select_user_button = tk.Button(self._window, text="Select User", command=self.select_user)
        self._select_user_button.pack(side='top',  fill='both',  padx=10,  pady=40,  expand=True)
        self._new_user_button = tk.Button(self._window, text="New User", command=self.new_user)
        self._new_user_button.pack(side='top',  fill='both',  padx=10,  pady=40,  expand=True)
        self._quickplay_button = tk.Button(self._window, text="Quick Play", command=self.quickplay)
        self._quickplay_button.pack(side='top',  fill='both',  padx=10,  pady=40,  expand=True)
        self._help_button = tk.Button(self._window, text="Help", command=self.help)
        self._help_button.pack(side='right',  fill='both',  padx=10,  pady=40,  expand=False)

    def select_user(self):
        print(os.listdir(os.getcwd()+"/users"))
        if len(os.listdir(os.getcwd()+"/users")) < 1:
            response = messagebox.askyesno("Unable to find user", "No users were found!\nWould you like to create a new user?")
            if response:
                self.new_user()
                return
            else:
                return
        self._master.launch_choose_user(self)

    def new_user(self):
        self._master.launch_user_screen(source=self._window)
        #launch_user_screen(self._window)

    def quickplay(self):
        self._master.launch_play_game(source=self, quick_play=True)

    def help(self):
        pass

if __name__ == 'main':
    screens = []
    while True:
        if not screens:
            screen = LoginScreen(master=None)
            screens.append(screen)
            screen._window.mainloop()