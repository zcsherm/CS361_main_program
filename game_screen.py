import tkinter as tk
from doctest import master
from tkinter import messagebox
class GameScreen(tk.Toplevel):
    def __init__(self, master, player, quickplay):
        super().__init__()
        self.player = player
        self.quickplay=quickplay
        self._master = master
        self._window = self
        self.title("Play Ball")
        self._text_vars = [tk.StringVar() for i in range(15)]
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

        label = tk.Label(frame1,text="Play Ball!")
        label.pack(fill='both',pady=20, anchor='center')

        # Setup innings
        label = tk.Label(frame2,text='Away')
        label.grid(row=1,column=0)
        label = tk.Label(frame2,text='Home')
        label.grid(row=2,column=0)

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
        entry.grid(row=player_row,column=1)
        entry = tk.Entry(frame2)
        entry.insert(0,"Opponent")
        entry.grid(row=opponent_row,column=1)
        self.away_scores=[tk.IntVar()for i in range(9)]
        self.home_scores=[tk.IntVar() for i in range(9)]
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

        # Extra Innings:
        label = tk.Label(frame4,text='Extra Innings:')
        label.grid(row=0,column=0, columnspan=3,sticky='w')
        label = tk.Label(frame4)
        label.grid(row=1,column=1,pady=10,padx=30)
        for i in range(3):
            label = tk.Label(frame4,text=i+7)
            label.grid(row=0,column=i+2,padx=20)
            box=tk.Spinbox(frame4,from_=0,to=99,textvariable=self.away_scores[6+i],command=self.on_change,width=3)
            box.grid(row=1,column=i+2)
            box=tk.Spinbox(frame4,from_=0,to=99,textvariable=self.home_scores[6+i],command=self.on_change,width=3)
            box.grid(row=2,column=i+2)

        # Score
        label = tk.Label(frame5, text="Away")
        label.grid(row=0,column=0)
        label = tk.Label(frame5, text="Home")
        label.grid(row=0,column=2)
        self._away_score =tk.Label(frame5,text="0",font=("Arial", 36),foreground='blue')
        self._away_score.grid(row=1,column=0)
        self._home_score = tk.Label(frame5, text="0", font=("Arial", 36), foreground='red')
        self._home_score.grid(row=1, column=2)
        self._finish_game_button = tk.Button(frame5, text="Finish Game",command=self.finish)
        self._finish_game_button.grid(row=2,column=1)

    # Return
        self._return_button = tk.Button(frame6,text='Return',command=self.go_to_main)
        self._return_button.pack(side='right',padx=10,pady=10,anchor='e')


    def default_spin_boxes(self):
        for box in self.away_scores:
            box.set(0)
        for box in self.home_scores:
            box.set(0)

    def on_change(self):
        home_tot = 0
        away_tot = 0
        for i in range(9):
            home_tot += int(self.home_scores[i].get())
            away_tot += int(self.away_scores[i].get())
        self._current_score=(away_tot,home_tot)
        self._home_score.configure(text=home_tot)
        self._away_score.configure(text=away_tot)

    def finish(self):
        DisplayScore(self,self._current_score[0],self._current_score[1])

    def go_to_main(self):
        respone = messagebox.askyesno("Return?", "Returning will lose all progress in the current game. \nAre you sure?")
        if respone:
            if self.quickplay:
                self._master.launch_login(self)
            else:
                self._master.launch_home(self)
            return
        return

class DisplayScore(tk.Toplevel):
    def __init__(self,master,away_score,home_score):
        super().__init__()
        self._master=master
        self._window=self
        self._away_score=away_score
        self._home_score=home_score

        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=1)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the 6 main innings fields
        frame2.grid(row=1, column=0, columnspan=1)
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the instructions
        frame3.grid(row=2, column=0, columnspan=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the Extra Innings
        frame4.grid(row=3, column=0, columnspan=1)
        frame5 = tk.LabelFrame(self._window, borderwidth=0)  # For the score and finish button
        frame5.grid(row=4, column=0, columnspan=1)

        label = tk.Label(frame1, text="Final Score:")
        label.pack(fill='both')

        label = tk.Label(frame2, text=f"{self._away_score}",font=("Arial", 36),foreground='blue')
        label.grid(row=0,column=0)
        label = tk.Label(frame2, text = f" - ",font=("Arial",36))
        label.grid(row=0,column=1)
        label = tk.Label(frame2, text=f"{self._home_score}", font=("Arial", 36), foreground='red')
        label.grid(row=0, column=2)

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
        if not self._master.quickplay and not (self.winner is None):
            save = tk.Button(frame4,text="Save Game",command=self.save_game)
            save.pack()

        ret = tk.Button(frame5,text="Return",command=self.go_back)
        ret.grid(row=0,column=1)
        home = tk.Button(frame5, text="Home", comman=self.go_home)
        home.grid(row=0,column=2)

    def save_game(self):
        response = messagebox.askyesno("Are you sure?",f"The current season is {self._master._master.user.get_current_season()}, would you like to save the game to this season's standings?")
        if self.winner==self._master.player:
            outcome = 'w'
        else:
            outcome = 'l'
        if response:
            self._master._master.user.add_game_to_season(outcome)
            self.go_home()

    def go_back(self):
        self.destroy()

    def go_home(self):
        if self._master.quickplay:
            self.destroy()
            self._master._master.launch_login(self._master)
        else:
            self.destroy()
            self._master._master.launch_home(self._master)