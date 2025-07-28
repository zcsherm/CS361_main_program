import tkinter as tk
from tkinter import messagebox
import os

class SelectSeason(tk.Toplevel):
    """
    The select a season screen. Displays all the users seasons with corresponding radio buttons
    """
    def __init__(self,master):
        """
        Initialize the page
        :master: the main launcher for the page
        """
        # Setup the basic attributes
        super().__init__()
        self._master = master
        self._window = self
        self.title("Choose a Season")
        
        # Get all of the users seasons and shift focus if not already shifted
        seasons = self._master.user.get_seasons()
        self.focus_set()

        # Setup all the frames for the page
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=3)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the seasons
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the cancel button
        frame3.grid(row=2, column=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the submit button
        frame4.grid(row=2, column=0)


        # Setup the title label
        label = tk.Label(frame1, text=f"Please Choose a season:\n(the current season is {self._master.user.get_current_season()} ")
        label.pack()

        # Setup the cancel button, submit buttons, and the hotkeys for each
        self._cancel_button = tk.Button(frame4, text="Cancel", command=self.go_to_home,underline=0)
        self._cancel_button.pack(side='left', padx=10, pady=10)
        self._submit_button = tk.Button(frame3, text="Submit", command=self.change_season,underline=0)
        self._submit_button.pack(side='right', padx=10, pady=10)
        self.bind('<Alt-c>', self.go_to_home)
        self.bind('<Alt-s>', self.change_season)

        # Setup the radio buttons for each season
        self._selected_season = tk.StringVar()
        self._selected_season.set("None")
        for i in range(len(seasons)):
            text = seasons[i]
            radio = tk.Radiobutton(frame2,text=text,variable=self._selected_season, value=text)
            radio.pack()


    def go_to_home(self,event=None):
        """
        Returns back to the home screen
        """
        self._master.launch_home(self)

    def change_season(self, event=None):
        """
        Updates the current selected season, asks user if they want to proceed
        """
        # Verify that the user wants to proceed
        response = messagebox.askyesno("Continue?","Changing the season will cause future games and team adjustments to be recorded in the selected season.\nAre you sure you wish to proceed?")
        # If they do, change the users season and go back to home
        if response:
            self._master.change_season(self._selected_season.get())
            self._master.launch_home(self)
        else:
            return
