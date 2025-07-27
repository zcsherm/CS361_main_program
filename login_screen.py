from tkinter import messagebox, ttk
import tkinter as tk
import os
from pagetext import *

# Add frames for spacing the buttons
# Add proper window geometry

class LoginScreen(tk.Toplevel):
    def __init__(self, master):
        #self._window = tk.Tk()
        #self._window.config(width=600, height=600)
        #self._window.title("Welcome")
        super().__init__()
        self._window= self
        self.title("welcome")
        self._master = master

        txt1 = "Welcome to the tracker for Baseball Highlights: 2045!"
        label = tk.Label(self._window, text=txt1)
        label.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)
        label = tk.Label(self._window, text = 'Please make a selection below')
        label.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)
        frame1 = tk.LabelFrame(self)
        frame1.pack(side='top',padx=10,pady=5)
        self._select_user_button = tk.Button(frame1, text="Select User", command=self.select_user,width=20)
        self._select_user_button.pack(side='top', padx=10,  pady=20)
        self._new_user_button = tk.Button(frame1, text="New User", command=self.new_user,width=20)
        self._new_user_button.pack(side='top',  padx=10,  pady=20)
        self._quickplay_button = tk.Button(frame1, text="Quick Play", command=self.quickplay,width=20)
        self._quickplay_button.pack(side='top',  padx=10,  pady=20)
        self._help_button = tk.Button(self, text="Help", command=self.help)
        self._help_button.pack(side='right',  fill='both',  padx=10,  pady=20,  expand=False)

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
        Help(self)

class Help(tk.Toplevel):
    def __init__(self,master):
        super().__init__()
        self.title(LOGIN_HELP_TITLE)
        self._window = self
        self._master=master
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=2)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # subtitle
        frame2.grid(row=1, column=0, columnspan=2)
        frame3 = tk.LabelFrame(self._window)  # For help descriptions
        frame3.grid(row=2, column=0, sticky='w')
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For return button
        frame4.grid(row=2, column=1, sticky='s')
        label = tk.Label(frame1,text=LOGIN_HELP_TITLE)
        label.pack(fill='both', padx=10, pady=5, expand=True)
        label = tk.Label(frame2,text = LOGIN_HELP_SUBTITLE)
        label.pack(fill='both',padx=10,pady=5,expand=True)
        label = tk.Label(frame3, text=LOGIN_HELP_DESCRIPTION,justify='left',wraplength=200)
        label.pack(padx=10,pady=5,side='left')
        button=tk.Button(frame4,text=LOGIN_HELP_RETURN_BUTTON,command=self.go_back)
        button.pack(padx=10,pady=5,anchor='s')

    def go_back(self):
        self.destroy()
