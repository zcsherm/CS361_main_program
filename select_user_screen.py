import tkinter as tk
import os

class SelectUser(tk.Toplevel):
    """
    A screen to select a user, displays all users as radio buttons
    """
    def __init__(self,master):
        # setup attributes
        super().__init__()
        self._master = master
        self._window = self
        self.title("Choose a User")

        # Fetch all the files in the user directory
        directories =[]
        path = os.getcwd()+'/users'
        for dir in os.listdir(path):
            directories.append(dir)
        self.focus_set()

        # Setup the frames
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=3)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the users radio buttons
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the submit button
        frame3.grid(row=2, column=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the cancel button
        frame4.grid(row=2, column=0)

        # Setup the title
        label = tk.Label(frame1, text="Please Choose a User:")
        label.pack()

        # Setup the buttons and hotkeys
        self._cancel_button = tk.Button(frame4, text="Cancel", command=self.go_to_main, underline=0)
        self._cancel_button.pack(side='left', padx=10, pady=40)
        self._submit_button = tk.Button(frame3, text="Submit", command=self.load_user, underline=0)
        self._submit_button.pack(side='right', padx=10, pady=40)
        self.bind('<Alt-s>', self.load_user)
        self.bind('<Alt-c>', self.go_to_main)

        # Setup a the radio buttons and the variable
        self._selected_user = tk.StringVar()
        self._selected_user.set("None")
        for i in range(len(directories)):
            text = directories[i][0:-4] # Drops the '.pkl'
            radio = tk.Radiobutton(frame2,text=text,variable=self._selected_user, value=directories[i])
            radio.pack()


    def go_to_main(self,event=None):
        """
        Returns to the login screen
        """
        self._master.launch_login(self)

    def load_user(self, event=None):
        """
        Pulls the requested user info and goes to the home screen.
        """
        self._master.get_user(self._selected_user.get()[0:-4])
        self._master.launch_home(self)
