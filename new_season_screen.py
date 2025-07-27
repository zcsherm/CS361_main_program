from tkinter import messagebox, ttk
import tkinter as tk

INSTRUCTIONS_YEAR = "Labelling the year helps organize individual long plays. Using a number is recommended"
INSTRUCTIONS_GAME = "Determines how many games are in the regular season. The recommended is 33 games."
INSTRUCTIONS_TEAM = "Checking this box will take you to the team setup page."
class AddSeasonScreen(tk.Toplevel):
    def __init__(self,master=None, data=None):
        super().__init__()
        self._window = self
        self.title("New Season")
        self._master=master
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=2)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For year entry
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window)  # For description of year
        frame3.grid(row=1, column=1)
        frame4 = tk.LabelFrame(self._window,borderwidth=0)  # For num of games
        frame4.grid(row=2, column=0,sticky='w')
        frame5 = tk.LabelFrame(self._window)  # For description of num of games
        frame5.grid(row=2, column=1)
        frame6 = tk.LabelFrame(self._window, borderwidth=0)  # For add init team
        frame6.grid(row=3, column=0,sticky='w')
        frame7 = tk.LabelFrame(self._window)  # for description of add team
        frame7.grid(row=3, column=1)
        frame9 = tk.LabelFrame(self._window,borderwidth =0)
        frame9.grid(row=4, column =1,rowspan=7)
        frame8 = tk.LabelFrame(self._window, borderwidth=0)  # For buttones
        frame8.grid(row=4, column=0, columnspan=2,sticky='s') # For adding buttons
        label = tk.Label(frame1, text="Create a New Season:")
        label.pack(side=tk.TOP,  fill='both',  padx=10,  pady=5,  expand=True)
        label = tk.Label(frame2, text = "Year:")
        label.pack(side="left",padx=10, pady=5)
        self._year_var = tk.StringVar()
        self._year_entry = tk.Entry(frame2, width= 15, textvariable=self._year_var)
        self._year_entry.pack(side="left",padx=10, pady=5)
        label = tk.Label(frame3, text=INSTRUCTIONS_YEAR, wraplength=100)
        label.pack()
        label = tk.Label(frame4, text="Number of Games:")
        label.pack(side="left", fill='both', padx=10, pady=5)
        self._games_var = tk.IntVar(value=33)
        self._games = tk.Spinbox(frame4,from_=3,to=99, increment=3, textvariable=self._games_var,width=3)
        self._games.pack(side="left", fill='both', padx=10, pady=5)
        label = tk.Label(frame5, text=INSTRUCTIONS_GAME, wraplength=100)
        label.pack()
        #label = tk.Label(frame6, text="Add initial team:")
        #label.pack(side="left", fill='both', padx=10, pady=5)
        self._team_var = tk.IntVar()
        self._team = tk.Checkbutton(frame6,text="Add Initial Team",variable=self._team_var, onvalue=1,offvalue=0,padx=15)
        self._team.pack()
        label = tk.Label(frame7, text = INSTRUCTIONS_TEAM, wraplength=100)
        label.pack()
        label = tk.Label(frame9, text = "\n\n\n\n\n")
        label.pack()
        self._return_button = tk.Button(frame8, text="Cancel", command=self.go_to_home,underline=0)
        self._return_button.pack(side='bottom', padx=10, pady=10)
        self._add_season_button = tk.Button(frame8, text="Add", command=self.add_season,underline=0)
        self._add_season_button.pack(side='bottom', padx=10, pady=10)
        self.bind('<Alt-c>', self.go_to_home)
        self.bind('<Alt-a>', self.add_season)

    def add_season(self,event=None):
        print(self._games_var.get())
        print(self._team_var.get())
        print(self._year_var.get())
        self._master.user.add_season(self._year_var.get(),num_of_games=self._games_var.get())
        self._master.save_user()
        if self._team_var.get() == 1:
            self._master.launch_team(self)
            return
        self.go_to_home()
        pass

    def go_to_home(self,event=None):
        self._master.launch_home(self)