# Python Course - Steps 262 & 264 ("Phonebook App, Pts 1 & 2")
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
        self.master.minsize(500, 300) # (height, width)
        self.master.maxsize(500, 300)
        phonebook_fun.center_window(self, 500, 300) # '.center_window()': centers app on the user's screen
        self.master.title("The Tkinter Phonebook Demo") # window's title
        self.master.configure(bg = "#FOFOFO") # window's background color
        
        # '.protocol()': built-in tkinter method; this one checks if "X" in WindowsOS was clicked:
        self.master.protocol("WM_DELETE-WINDOW", lambda: phonebook_func.ask_quit(self))

        # loads the GUI widgets from a seperate module, keeping code
        # compartmentalized & clutter-free
        phonebook_gui.load_gui(self)

          


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 
