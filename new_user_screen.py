from tkinter import messagebox, ttk
import tkinter as tk
import Pmw
# Add text as CONSTANTS (maybe in a separate file)
# Add hover alert over season
# Add calls to launch player screen and season screen

INSTRUCTIONS = "This process will walk you through setting up a new user, new season, and a new team."
class AddUserScreen(tk.Toplevel):
    def __init__(self,master=None, data=None):

        #self._window = tk.Tk()
        #self._window.config(width=600, height=600)
        #self._window.title("New User")
        super().__init__()
        self._window = self
        self.title("New User")
        self._master=master
        Pmw.initialise(self._master.root)
        frame1 = tk.LabelFrame(self._window,borderwidth=0) # For the title
        frame1.grid(row=0,column=0,columnspan=3)
        frame2 = tk.LabelFrame(self._window, borderwidth=0) # For enter name
        frame2.grid(row=1, column=0)
        frame3 = tk.LabelFrame(self._window,borderwidth=0) # For enter field
        frame3.grid(row=1, column=1)
        frame4 = tk.LabelFrame(self._window) # For instruction
        frame4.grid(row=1, column=2, rowspan=1)
        frame5 = tk.LabelFrame(self._window,borderwidth=0) # For buttons
        frame5.grid(row=2, column=1)
        txt1 = "Please enter your name:"
        label = tk.Label(frame1, text=txt1)
        label.pack(side='top',  fill='both',  padx=10,  pady=5,expand=False)
        label = tk.Label(frame4, text = INSTRUCTIONS, wraplength=100)
        label.pack(side=tk.TOP,  fill='both',  padx=10,  pady=5,  expand=True)
        label = tk.Label(frame2, text='Name:')
        label.pack(anchor='n',padx=10,pady=5,expand=False, fill='none')
        self._name_var = tk.StringVar()
        self._entry = tk.Entry(frame3,width = 20,textvariable=self._name_var)
        self._entry.pack(side='top',padx=10,pady=5)
        self._add_user_button = tk.Button(frame5, text="Add", command=self.add_user, underline =0)
        self._add_user_button.pack(side='top',  fill='both',  padx=10,  pady=10,  expand=True)
        self._return_button = tk.Button(frame5, text="Return", command=self.go_to_main, underline=0)
        self._return_button.pack(side='top',  fill='both',  padx=10,  pady=10,  expand=True)
        self.bind('<Alt-r>', self.go_to_main)
        self.bind('<Alt-a>', self.add_user)
        self.focus_set()

    def add_user(self, event=None):
        #response = messagebox.askyesno("Add season", "Would you like to create a starting season?")
        self.response = Pmw.MessageDialog(self._master.root,
                                        title="Create Season?",
                                        message_text="Would you like to create a starting season?.",
                                        buttons=('Add Season','Skip for now',),
                                     command = self.season_add)
        self.response.focus_set()
        hover = Pmw.Balloon(self._master.root)
        hover.bind(self.response.interior(), 'A season lets you record progress over a large series of games')

    def go_to_main(self,event=None):
        response = messagebox.askyesno("Return to main menu?", "This will return you to the home screen, any unsaved changes will be lost. Are you sure?")
        if response:
            self._master.launch_login(self)
        else:
            return

    def season_add(self, selected):
        if selected == 'Add Season':
            self.response.withdraw()
            name = self._entry.get()
            print(name)
            print(self._name_var.get())
            self._master.new_user(self._name_var.get())
            self._master.save_user()
            self._master.launch_new_season(self)
        else:
            self.response.withdraw()
            name = self._entry.get()
            self._master.new_user(self._name_var.get())
            self._master.save_user()
            self._master.launch_home(self)


