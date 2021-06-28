# Python Course - Steps 262 ("Phonebook App, Pt 1")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
# -------------------------------------
# Objective: design a phonebook app, employing
#            advanced features such as a
#            GUI and attached database
# -------------------------------------

# Imports tkinter & all of its widgets:
import tkinter as tk
from tkinter import * # allows unpacking of ALL of tkinter's widgets
# Imports other forms:
import phonebook_gui
import phonebook_func


# Blueprints for creating a tkinter 'window':
class ParentWindow(Frame): # 'Frame' is the PARENT CLASSS within tkinter 
    def __init__(self, master, *args, **kwargs):
        Frame:__init__(self, master, *args, **kwargs)

        # The displayed window:
        self.master = master
        self.master.minsize(500, 300) # (Height, Width)
        self.master.maxsize(500, 300)
        # This CenterWindow method will center our app on the user's screen:
        phonebook_fun.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(b="#FOFOFO")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS:
        self.master.protocol("WM_DELETE-WINDOW", lamda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        # keeping your code compartmentalized & clutter-free
        phonebook_gui.load_gui(self)

          


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 
