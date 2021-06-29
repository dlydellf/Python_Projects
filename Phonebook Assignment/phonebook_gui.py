# Python Course - Step 266 ("Phonebook App, Pt. 3")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
# -------------------------------------
# Objective: design a phonebook app, employing
#            advanced features such as a
#            GUI and attached database
# -------------------------------------


# Imports tkinter & all of its widgets:
from tkinter import *
import tkinter as Tk # allows unpacking of ALL of tkinter's widgets
# Imports other forms:
import phonebook_main
import phonebook_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master, text='First Name:')
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name:')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text='Email Address:')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), stick=N+W)
    self.lbl_user = tk.Label(self.master, text='User:')
    self.lbl_user.grid(riow=0, column=2, padx=(0,0, pady=(10,0), sticky=N+W)
    

