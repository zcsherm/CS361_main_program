import tkinter as tk
from pagetext import *
class HomeScreen(tk.Toplevel):
    def __init__(self,master=None, data=None):
        super().__init__()

        self._window = self
        self.title("Home")
        self._master=master
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=4)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For add season button
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window)  # For Players
        frame3.grid(row=1, column=3,rowspan=3)
        frame4 = tk.LabelFrame(self._window,borderwidth=0)  # For select season button
        frame4.grid(row=2, column=0,sticky='w')
        frame5 = tk.LabelFrame(self._window,borderwidth=0)  # For update team button
        frame5.grid(row=3, column=0,sticky='w')
        frame6 = tk.LabelFrame(self._window, borderwidth=0)  # play game button
        frame6.grid(row=4, column=1,sticky='s')
        frame7 = tk.LabelFrame(self._window, borderwidth=0)  # for help button
        frame7.grid(row=4, column=0, stick='w')

        label = tk.Label(frame1, text=f"Welcome {self._master.user.get_name()}!\nYour current season is {self._master.user.get_current_season()}")
        label.pack(fill='both',  padx=10,  pady=5,  expand=True)
        if (self._master.user.get_current_season() is not None):
            wins, losses, games = self._master.user.get_win_loss()
            label = tk.Label(frame1,text=f"Your current standing is {wins}-{losses} of {games} games")
            label.pack(fill='both',padx=10,pady=5,expand=True)
        self._add_season_button = tk.Button(frame2, text="Add Season", command=self.add_season)
        self._add_season_button.pack(side='left', padx=10, pady=40)
        self.setup_team_frame(frame3)
        self._select_season_button = tk.Button(frame4, text="Select Season", command=self.select_season)
        self._select_season_button.pack(side='left', padx=10, pady=40)
        self._update_team_button = tk.Button(frame5, text="Update Team", command=self.update_team)
        self._update_team_button.pack(side='left', padx=10,pady=40)
        self._add_season_button.pack(side='left', padx=10, pady=40)
        self._add_season_button = tk.Button(frame6, text="Play Game!", command=self.play_game)
        self._add_season_button.pack(side='bottom', padx=10, pady=40)
        self._help_button = tk.Button(frame7, text="Help", command=self.help)
        self._help_button.pack(side='left', padx=10, pady=40)

    def setup_team_frame(self,frame):
        team = self._master.user.get_current_team()
        txt = "Current Team:\n\n"
        for i in range(15):
            #new_frame = tk.LabelFrame(frame, borderwidth=0)  # For update team button
            #new_frame.grid(row=i+1, column=0, sticky='w',pady=0)
            #new_txt = f"{i}. {team[i]}\n"
            txt += f"{i+1}. {team[i]}\n"
            #new_label = tk.Label(new_frame, text=new_txt,)
            #new_label.pack(anchor='w',pady=0)
        label = tk.Label(frame, text =txt,justify='left')
        label.grid(row=0,column=0)

    def add_season(self):
        self._master.launch_new_season(self)
        pass

    def select_season(self):
        self._master.launch_select_season(self)

    def update_team(self):
        self._master.launch_team(self)

    def play_game(self):
        self._master.launch_play_game(self)

    def help(self):
        Help(self)

class Help(tk.Toplevel):
    def __init__(self,master):
        super().__init__()
        self.title(HOME_HELP_TITLE)
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
        label = tk.Label(frame1,text=HOME_HELP_TITLE)
        label.pack(fill='both', padx=10, pady=5, expand=True)
        label = tk.Label(frame2,text = HOME_HELP_SUBTITLE)
        label.pack(fill='both',padx=10,pady=5,expand=True)
        label = tk.Label(frame3, text=HOME_HELP_DESCRIPTION,justify='left')
        label.pack(padx=10,pady=5,side='left')
        button=tk.Button(frame4,text=HOME_HELP_RETURN_BUTTON,command=self.go_back)
        button.pack(padx=10,pady=5,anchor='s')

    def go_back(self):
        self.destroy()
