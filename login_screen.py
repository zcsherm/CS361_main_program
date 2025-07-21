from tkinter import messagebox, ttk
import tkinter as tk

class LoginScreen:
    def __init__(self):
        self._window = tk.Tk()
        self._window.config(width=600, height=600)
        self._window.title("Welcome")
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
        self._select_user_button.pack(side='top',  fill='both',  padx=10,  pady=40,  expand=True)
        self._help_button = tk.Button(self._window, text="Help", command=self.help)
        self._help_button.pack(side='right',  fill='both',  padx=10,  pady=40,  expand=False)

    def select_user(self):
        pass
    def new_user(self):
        pass
    def quickplay(self):
        pass
    def help(self):
        pass
        
