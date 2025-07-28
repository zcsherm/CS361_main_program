import tkinter as tk
from tkinter import messagebox

class GameScreen(tk.Toplevel):
    """
    The screen for entering in the results of a single game
    """
    def __init__(self, master, player, quickplay):
        """
        Initialize the screen
        :master: The launcher
        :player: whether the player is 'home' or 'away'
        :quickplay: boolean, True if this page was launched from the login screen
        """
        # Setup basic attributes
        super().__init__()
        self.player = player
        self.quickplay=quickplay
        self._master = master
        self._window = self
        self._current_score = (0,0)
        self.title("Play Ball")
        self.focus_set()

        # Setup the frames
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=4)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the 6 main innings fields
        frame2.grid(row=1, column=0, columnspan=4)
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the instructions
        frame3.grid(row=2, column=0, columnspan=4)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the Extra Innings
        frame4.grid(row=3, column=0, columnspan=2)
        frame5 = tk.LabelFrame(self._window, borderwidth=0)  # For the score and finish button
        frame5.grid(row=3, column=2, columnspan=2)
        frame6 = tk.LabelFrame(self._window, borderwidth=0)  # For the return button
        frame6.grid(row=4, column=3, columnspan=1,stick='se')

        # Create the label for the title
        label = tk.Label(frame1,text="Play Ball!")
        label.pack(fill='both',pady=20, anchor='center')

        # Setup innings frame
        label = tk.Label(frame2,text='Away')
        label.grid(row=1,column=0)
        label = tk.Label(frame2,text='Home')
        label.grid(row=2,column=0)

        # Put the player in the correct row based on home or away
        if quickplay:
            player_text='Player 1'
        else:
            player_text = self._master.user.get_name()
        entry = tk.Entry(frame2)
        entry.insert(0,player_text)
        if self.player=='away':
            player_row =1
            opponent_row=2
        else:
            player_row=2
            opponent_row=1

        # place entry fields for the players name and opponent
        entry.grid(row=player_row,column=1)
        entry = tk.Entry(frame2)
        entry.insert(0,"Opponent")
        entry.grid(row=opponent_row,column=1)

        # Setup variables for spinboxes
        self.away_scores=[tk.IntVar()for i in range(9)]
        self.home_scores=[tk.IntVar() for i in range(9)]

        # Place spin boxes for each inning
        for i in range(6):
            label = tk.Label(frame2,text=i+1)
            label.grid(row=0,column=i+2,padx=20)
            box=tk.Spinbox(frame2,from_=0,to=99,textvariable=self.away_scores[i],command=self.on_change,width=3)
            box.grid(row=1,column=i+2)
            box=tk.Spinbox(frame2,from_=0,to=99,textvariable=self.home_scores[i],command=self.on_change,width=3)
            box.grid(row=2,column=i+2)

        # setup instructions
        txt = "Record both teams names and each runs scored in each inning"
        label = tk.Label(frame3, text=txt)
        label.pack(fill='both',pady=20,expand=True)

        # Setup extra innings
        label = tk.Label(frame4,text='Extra Innings:')
        label.grid(row=0,column=0, columnspan=3,sticky='w')
        label = tk.Label(frame4)
        label.grid(row=1,column=1,pady=10,padx=30)

        # Place the 2 spinboxes for ech extra inning
        for i in range(3):
            label = tk.Label(frame4,text=i+7)
            label.grid(row=0,column=i+2,padx=20)
            box=tk.Spinbox(frame4,from_=0,to=99,textvariable=self.away_scores[6+i],command=self.on_change,width=3)
            box.grid(row=1,column=i+2)
            box=tk.Spinbox(frame4,from_=0,to=99,textvariable=self.home_scores[6+i],command=self.on_change,width=3)
            box.grid(row=2,column=i+2)

        # Setup the score frame
        label = tk.Label(frame5, text="Away")
        label.grid(row=0,column=0)
        label = tk.Label(frame5, text="Home")
        label.grid(row=0,column=2)
        self._away_score =tk.Label(frame5,text="0",font=("Arial", 36),foreground='blue')
        self._away_score.grid(row=1,column=0)
        self._home_score = tk.Label(frame5, text="0", font=("Arial", 36), foreground='red')
        self._home_score.grid(row=1, column=2)

        #Setup the finish button and hotkey
        self._finish_game_button = tk.Button(frame5, text="Finish Game",command=self.finish,underline=0)
        self._finish_game_button.grid(row=2,column=1)
        self.bind('<Alt-f>', self.finish)

        # Setup the return button and hotkey
        self._return_button = tk.Button(frame6,text='Return',command=self.go_to_main, underline=0)
        self._return_button.pack(side='right',padx=10,pady=10,anchor='e')
        self.bind('<Alt-r>', self.go_to_main)


    def default_spin_boxes(self):
        """
        Resets every spinbox to 0
        """
        for box in self.away_scores:
            box.set(0)
        for box in self.home_scores:
            box.set(0)

    def on_change(self):
        """
        When a spinbox is changed, the total score is recalculated
        """
        home_tot = 0
        away_tot = 0
        # Check the score in each spinbox
        for i in range(9):
            home_tot += int(self.home_scores[i].get())
            away_tot += int(self.away_scores[i].get())
        self._current_score=(away_tot,home_tot)
        self._home_score.configure(text=home_tot)
        self._away_score.configure(text=away_tot)

    def finish(self, event=None):
        """
        Ends the game at the current score
        """
        DisplayScore(self,self._current_score[0],self._current_score[1])

    def go_to_main(self, event=None):
        """
        Returns back to either the login screen or the home screen
        """
        # Asks user to confirm they want to exit0
        respone = messagebox.askyesno("Return?", "Returning will lose all progress in the current game. \nAre you sure?")
        if respone:
            if self.quickplay:
                self._master.launch_login(self)
            else:
                self._master.launch_home(self)
            return
        return

class DisplayScore(tk.Toplevel):
    """
    The window which displays the final score and the winner
    """
    def __init__(self,master,away_score,home_score):
        """
        Initialize the screen
        :master: The game screen that launched this
        :away_score: The score of the away team
        :home_score: The score of the home team
        """
        super().__init__()
        # Setup attributes
        self._master=master
        self._window=self
        self._away_score=away_score
        self._home_score=home_score
        self.focus_set()

        # Setup the frames
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=1)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the score
        frame2.grid(row=1, column=0, columnspan=1)
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the winner
        frame3.grid(row=2, column=0, columnspan=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the save button
        frame4.grid(row=3, column=0, columnspan=1)
        frame5 = tk.LabelFrame(self._window, borderwidth=0)  # For the return and home button
        frame5.grid(row=4, column=0, columnspan=1)

        # Setup the title
        label = tk.Label(frame1, text="Final Score:")
        label.pack(fill='both')

        # Setup the score display
        label = tk.Label(frame2, text=f"{self._away_score}",font=("Arial", 36),foreground='blue')
        label.grid(row=0,column=0)
        label = tk.Label(frame2, text = f" - ",font=("Arial",36))
        label.grid(row=0,column=1)
        label = tk.Label(frame2, text=f"{self._home_score}", font=("Arial", 36), foreground='red')
        label.grid(row=0, column=2)

        # Setup the winner
        if self._home_score > self._away_score:
            self.winner='home'
            text = "Home Team wins!"
        elif self._home_score != self._away_score:
            self.winner='away'
            text = "Away Team wins!"
        else:
            self.winner=None
            text = "Nobody won! Keep going in extra innings!"
        label = tk.Label(frame3, text=text)
        label.pack(fill='both')

        # Setup the save button and hotkey
        if not self._master.quickplay and not (self.winner is None):
            save = tk.Button(frame4,text="Save Game",command=self.save_game, underline=0)
            save.pack()
            self.bind('<Alt-s>', self.save_game)

        # Setup the return and homebutton and hotkeys.
        ret = tk.Button(frame5,text="Return",command=self.go_back,underline=0)
        ret.grid(row=0,column=1)
        home = tk.Button(frame5, text="Home", comman=self.go_home, underline=0)
        home.grid(row=0,column=2)
        self.bind('<Alt-r>', self.go_back)
        self.bind('<Alt-h>', self.go_home)

    def save_game(self, event=None):
        """
        Saves the result of the current game to the user object.
        """
        # Verifies that the user wants to save this game to the current season
        response = messagebox.askyesno("Are you sure?",f"The current season is {self._master._master.user.get_current_season()}, would you like to save the game to this season's standings?")

        # Determines how to record the game
        if self.winner==self._master.player:
            outcome = 'w'
        else:
            outcome = 'l'

        # Saves the game to the user, returns home
        if response:
            self._master._master.user.add_game_to_season(outcome)
            self._master._master.save_user()
            self.go_home()

    def go_back(self, event=None):
        """
        Returns back to the game screen
        """
        # Shift focus back and destroy this screen
        self._master.focus_set()
        self.destroy()

    def go_home(self,event=None):
        """
        Returns back to the home screen or the login screen
        """
        if self._master.quickplay:
            self.destroy()
            self._master._master.launch_login(self._master)
        else:
            self.destroy()
            self._master._master.launch_home(self._master)
