import tkinter as tk
from tkinter import messagebox
from pagetext import *
import communication_utilities as cu

PIPE = 'score_pipe.txt'

class HomeScreen(tk.Toplevel):
    """
    The users home screen
    """
    def __init__(self,master=None, data=None):
        # setup attributes
        super().__init__()
        self._window = self
        self.title("Home")
        self._master=master
        self.focus_set()

        # Setup all the frames
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
        self._update_team_button = tk.Button(self._window, text="Show High Scores", command=self.show_high_scores,underline=3)
        self._update_team_button.grid(row=4, column=0, sticky='w')
        frame6 = tk.LabelFrame(self._window, borderwidth=0)  # play game button
        frame6.grid(row=4, column=1,sticky='s')
        frame7 = tk.LabelFrame(self._window, borderwidth=0)  # for help button
        frame7.grid(row=5, column=0, stick='w')

        # Setup the title frame
        label = tk.Label(frame1, text=f"Welcome {self._master.user.get_name()}!\nYour current season is {self._master.user.get_current_season()}")
        label.pack(fill='both',  padx=10,  pady=5,  expand=True)
        if (self._master.user.get_current_season() is not None):
            wins, losses, games = self._master.user.get_win_loss()
            label = tk.Label(frame1,text=f"Your current standing is {wins}-{losses} of {games} games")
            label.pack(fill='both',padx=10,pady=5,expand=True)

        # Setup the add season button
        self._add_season_button = tk.Button(frame2, text="Add Season", command=self.add_season,underline=0)
        self._add_season_button.pack(side='left', padx=10, pady=40)

        # Setup all the player names
        self.setup_team_frame(frame3)

        # Setup the select season button
        self._select_season_button = tk.Button(frame4, text="Select Season", command=self.select_season,underline=0)
        self._select_season_button.pack(side='left', padx=10, pady=40)

        # Setup the update team button
        self._update_team_button = tk.Button(frame5, text="Update Team", command=self.update_team,underline=0)
        self._update_team_button.pack(side='left', padx=10,pady=40)


        # Setup the play button button
        self._play_button = tk.Button(frame6, text="Play Game!", command=self.play_game,underline=0)
        self._play_button.pack(side='bottom', padx=10, pady=40)
        self._play_button = tk.Button(frame6, text="Submit Score", command=self.save_season_score,underline=2)
        self._play_button.pack(side='bottom', padx=10, pady=40)

        # Setup the help button
        self._help_button = tk.Button(frame7, text="Help", command=self.help, underline=0)
        self._help_button.pack(side='left', padx=10, pady=40)

        # Setup all the hot keys
        self.bind('<Alt-a>', self.add_season)
        self.bind('<Alt-s>', self.select_season)
        self.bind('<Alt-u>', self.update_team)
        self.bind('<Alt-p>', self.play_game)
        self.bind('<Alt-h>', self.help)
        self.bind('<Alt-b>', self.save_season_score)


    def setup_team_frame(self,frame):
        """
        Creates a label which displays all the player names on the current team
        :frame: The frame to pack this label in
        """
        # Get the current team
        team = self._master.user.get_current_team()
        txt = "Current Team:\n\n"

        # Display the name of each player on a new line
        for i in range(15):
            txt += f"{i+1}. {team[i]}\n"
        label = tk.Label(frame, text =txt,justify='left')
        label.grid(row=0,column=0)

    def add_season(self,event=None):
        """
        Launches the add season screen
        """
        self._master.launch_new_season(self)

    def select_season(self,event=None):
        """
        Launches the select season screen
        """
        self._master.launch_select_season(self)

    def update_team(self,event=None):
        """
        Launches the update team Screen
        """
        self._master.launch_team(self)

    def play_game(self,event=None):
        """
        Launches the play game screen
        """
        self._master.launch_play_game(self)

    def help(self,event=None):
        """
        OPens the help screen
        """
        Help(self)

    def save_season_score(self):
        cu.read_write_cycle(PIPE, 'ADD')
        cu.read_write_cycle(PIPE, self._master.user.get_name())
        cu.read_write_cycle(PIPE, self._master.user.get_current_season())
        cu.read_write_cycle(PIPE, str(self._master.user.get_win_loss()[0]))
        content = cu.read_write_cycle(PIPE, str(self._master.user.get_win_loss()[1]))
        if content == '200':
            messagebox.showinfo("Success", "Your season information was successfully added")
        else:
            messagebox.showerror("Failure", f"Season score could not be saved. Response was {content}")

    def show_high_scores(self):
        HighScore(self)

class HighScore(tk.Toplevel):
    def __init__(self,master):
        super().__init__()
        self.title("High Scores")
        self._window = self
        self._master = master
        self.focus_set()
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=2)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame2.grid(row=1, column=0, columnspan=2)
        frame3 = tk.Button(self, text="Return", command=self.return_to_home)
        frame3.grid(row=2,column=0)

        label = tk.Label(frame1,text="All time highest season records")
        label.pack(fill='both', padx=10, pady=5, expand=True)

        cu.read_write_cycle(PIPE, "VIEW")
        contents = cu.read_write_cycle(PIPE, '10')
        scores = contents.split('\n')
        count = 1
        print(scores)
        for score in scores:
            if len(score) == 0:
                continue
            print(score)
            score = score.split(',')
            print(score[3])
            label = tk.Label(frame2, text = f"{count}. {score[0]} -- {score[1]} Season -- {score[2]}-{score[3]}")
            label.pack(fill = 'both', padx=10, pady=5, expand = True)
            count += 1
    def return_to_home(self):
        self._master.focus_set()
        self.destroy()

class Help(tk.Toplevel):
    """
    The help screen for the home page
    """
    def __init__(self,master):
        
        # Setup basic attibutes
        super().__init__()
        self.title(HOME_HELP_TITLE)
        self._window = self
        self._master=master
        self.focus_set()


        # Setup the frames
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=2)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # subtitle
        frame2.grid(row=1, column=0, columnspan=2)
        frame3 = tk.LabelFrame(self._window)  # For help descriptions
        frame3.grid(row=2, column=0, sticky='w')
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For return button
        frame4.grid(row=2, column=1, sticky='s')

        # Setup the title
        label = tk.Label(frame1,text=HOME_HELP_TITLE)
        label.pack(fill='both', padx=10, pady=5, expand=True)

        # Setup the subtitle
        label = tk.Label(frame2,text = HOME_HELP_SUBTITLE)
        label.pack(fill='both',padx=10,pady=5,expand=True)

        # Setup the help descriptions
        label = tk.Label(frame3, text=HOME_HELP_DESCRIPTION,justify='left')
        label.pack(padx=10,pady=5,side='left')

        # Setup the return button and hotkey
        button=tk.Button(frame4,text=HOME_HELP_RETURN_BUTTON,command=self.go_back,underline=0)
        button.pack(padx=10,pady=5,anchor='s')
        self.bind('<Alt-r>', self.go_back)

    def go_back(self,event=None):
        """
        Returns back to the home screen
        """
        self._master.focus_set()
        self.destroy()
