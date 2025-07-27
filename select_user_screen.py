import tkinter as tk
import os

class SelectUser(tk.Toplevel):
    def __init__(self,master):
        super().__init__()
        self._master = master
        self._window = self
        self._title = "Choose a User"
        directories =[]
        path = os.getcwd()+'/users'
        for dir in os.listdir(path):
            directories.append(dir)

        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=3)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the player fields
        frame2.grid(row=1, column=0,sticky='w')
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the right side slements
        frame3.grid(row=2, column=1)
        frame4 = tk.LabelFrame(self._window, borderwidth=0)  # For the right side slements
        frame4.grid(row=2, column=0)



        label = tk.Label(frame1, text="Please Choose a User:")
        label.pack()
        self._cancel_button = tk.Button(frame4, text="Cancel", command=self.go_to_main)
        self._cancel_button.pack(side='left', padx=10, pady=40)
        self._submit_button = tk.Button(frame3, text="Submit", command=self.load_user)
        self._submit_button.pack(side='right', padx=10, pady=40)

        self._selected_user = tk.StringVar()
        self._selected_user.set("None")
        for i in range(len(directories)):
            text = directories[i][0:-4]
            radio = tk.Radiobutton(frame2,text=text,variable=self._selected_user, value=directories[i])
            radio.pack()


    def go_to_main(self):
        self._master.launch_login(self)

    def load_user(self):
        self._master.get_user(self._selected_user.get()[0:-4])
        self._master.launch_home(self)