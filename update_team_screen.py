import tkinter as tk
from tkinter import messagebox

class TeamScreen(tk.Toplevel):
    """
    The screen to change out the team composition
    """
    def __init__(self, master, team):
        # Setup attribute
        super().__init__()
        self._team = team
        self._master = master
        self._window = self
        self.title("Update Roster")
        self._text_vars = [tk.StringVar() for i in range(15)] # Creates a variable for each team member slot
        self.focus_set()

        # Setup the frames
        frame1 = tk.LabelFrame(self._window, borderwidth=0)  # For the title
        frame1.grid(row=0, column=0, columnspan=5)
        frame2 = tk.LabelFrame(self._window, borderwidth=0)  # For the player fields
        frame2.grid(row=1, column=0, columnspan=3)
        frame3 = tk.LabelFrame(self._window, borderwidth=0)  # For the right side slements
        frame3.grid(row=1, column=4, columnspan=1)

        # Setup the title
        label= tk.Label(frame1, text='Update Your Team Members')
        label.pack(pady=20, fill='both',expand=True)

        # Setup the team entry frame
        self.setup_team_frame(frame2)

        # Setup the rightside elements
        self.setup_elements(frame3)

    def setup_team_frame(self,frame):
        """
        Creates a label for the existing team members and an entry field as well
        """
        # Create a row for each team member consisting of their name and an entry field for the replacement
        for i in range(15):
            text = f"{i}. {self._team[i]} -> Update to: "
            label = tk.Label(frame,text=text)
            self._text_vars[i].set(self._team[i])
            entry = tk.Entry(frame, width = 40,textvariable=self._text_vars[i])
            label.grid(column=0,row=i,pady=5,padx=5)
            entry.grid(column=1,row=i,pady=5,padx=5)

    def setup_elements(self,frame):
        """
        Generates the instructions and the buttons
        """
        label = tk.Label(frame, text="Type in the names of any replacement players you've added to your roster", wraplength=100)
        label.pack()
        self._update_button = tk.Button(frame, text="Update", command=self.update_season,underline=0)
        self._cancel_button = tk.Button(frame, text="Cancel", command=self.cancel_update,underline=0)
        self._update_button.pack()
        self._cancel_button.pack()
        self.bind('<Alt-u>', self.update_season)
        self.bind('<Alt-c>', self.cancel_update)


    def update_season(self, event=None):
        """
        Updates the current seasons roster and saves the user data
        """
        counter=0
        changes_text = ""
        new_team = []
        # For each entry field, check if the entered name is different
        for i in range(15):
            new_name= str(self._text_vars[i].get())
            old_name = str(self._team[i])
            
            # If it is different then mark that this player was changed
            if new_name != old_name:
                new_team.append(new_name)
                counter += 1
                txt = f"{counter}-> Player {i}: {old_name} replaced by {new_name}\n"
                changes_text+= txt
            else:
                new_team.append(old_name)

        # Display all the changes to the user
        if counter != 0:
            message_box = "Here is a summary of your changes:\n\n" + changes_text
            response = messagebox.askyesno("Keep Changes?", message_box)
            
            # If the user confirms, then save the changes and go to the home page
            if response:
                # Save changes and launch the home page
                self._master.user.update_team(new_team)
                self._master.save_user()
                self._master.launch_home(self)
            else:
                return
        
        # If no changes were made, then display an error
        else:
            messagebox.showerror("No changes made!", "No changes were made to the roster!")
    

    def cancel_update(self, event=None):
        """
        Returns the user to the home page after confirming.
        """
        response = messagebox.askyesno("Return?","Unsaved changes to your roster will be lost.\nAre you sure you want to cancel?")
        if response:
            self._master.launch_home(self)
        return
