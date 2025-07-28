import tkinter as tk
from tkinter import messagebox
import os

class SelectSeason(tk.Toplevel):
    def __init__(self,master):
        super().__init__()
        self._master = master
        self._window = self
        self.title("Choose a Season")
        seasons = self._master.user.get_seasons()
        self.focus_set()
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=3)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the player fields
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the right side slements
        frame3.grid(row=2, column=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the right side slements
        frame4.grid(row=2, column=0)



        label = tk.Label(frame1, text=f"Please Choose a season:\n(the current season is {self._master.user.get_current_season()} ")
        label.pack()
        self._cancel_button = tk.Button(frame4, text="Cancel", command=self.go_to_home,underline=0)
        self._cancel_button.pack(side='left', padx=10, pady=10)
        self._submit_button = tk.Button(frame3, text="Submit", command=self.change_season,underline=0)
        self._submit_button.pack(side='right', padx=10, pady=10)
        self.bind('<Alt-c>', self.go_to_home)
        self.bind('<Alt-s>', self.change_season)
        self._selected_season = tk.StringVar()
        self._selected_season.set("None")
        for i in range(len(seasons)):
            text = seasons[i]
            radio = tk.Radiobutton(frame2,text=text,variable=self._selected_season, value=text)
            radio.pack()


    def go_to_home(self,event=None):
        self._master.launch_home(self)

    def change_season(self, event=None):
        response = messagebox.askyesno("Continue?","Changing the season will cause future games and team adjustments to be recorded in the selected season.\nAre you sure you wish to proceed?")
        if response:
            self._master.change_season(self._selected_season.get())
            self._master.launch_home(self)
        else:
            return