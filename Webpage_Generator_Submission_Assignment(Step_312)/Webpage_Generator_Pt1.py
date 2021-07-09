# Python Course - Steps 310 & 311 ("Webpage Generator", Pts 1 & 2)
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#------------------------------------
# Objective: Recreate a supplied GUI that allows users
#            to select a directory and show that directory
#            in a text field.
#------------------------------------

# Imports tkinter and all of its widgets:
import tkinter
from tkinter import * # Allows unpacking of ALL of tkinter's 'wdigets' (tkinter CLASS objects)
import webbrowser # Module that displays web-based docs


# Blueprint for creating the main window:
class ParentWindow(Frame): # 'Frame' is the PARENT CLASS within tkinter
    def __init__(self, master): # 'self' == the 'ParentWindow' class, 'master' == the Frame class
        Frame.__init__(self)

        # The displayed window:
        self.master = master
        self.master.geometry('{}x{}'.format(650, 260)) # Window's default size upon launching
        self.master.resizable(width=False, height=False) # User can resize window's x/y
        self.master.title('Webpage Generator, Pt.2') # Window's Title
        self.master.config(bg='lightgrey') # Window's background color

        # The LABEL:
        self.lbl = Label(self.master, text="Type the webpage's body\nin the box to the right,\n\nthen click 'Submit'\nto update the webpage.")
        self.lbl.place(x=5, y=5, width=140, height=220)
        
        # The TEXTBOX:
        # 'Entry' == tkinter widget; a single-line textbox that accepts input; 'self.master' is the ENTIRE window
        self.txtbx = Entry(self.master, text='')
        self.txtbx.place(x=150, y=5, width=495, height=250) # Textbox ABSOLUTELY positioned, since RESIZABLE=FALSE

        # The SUBMIT Button:
        self.btn_Submit = Button(self.master, width=7, height=1, text="Submit", command=lambda: nameOfFunction(self))
        self.btn_Submit.place(x=5, y=230, width=140)        

        # Displays the text:

# The script to generate webpages:
def pageGenerator():
    fileName = open("upcomingSale.html", "w") # Create new .txt file, name "upcomingSale" (if it doesn't already exist); overwrite any existing content
    fileName.write("<html>\n\t<body>\n\t\t<h1>\n\tStay tuned for our amazing Summer sale!\n\t\t</h1>\n\t</body>\n</html>") # .txt file's HTML
    fileName.close()
    webbrowser.open_new_tab('upcomingSale.html') # does NOT require 'http://' if directing to a file
            
#pageGenerator()

if __name__ == '__main__':
    root = Tk() # the object 'root' is created from the instantiated 'Tk()' (tkinter's PARENT CLASS)
    App = ParentWindow(root) # [(root === Frame) -> passed into 'ParentWindow'] -> assigned to 'App'
    root.mainloop() # Prevents window from launching, then immediately closing
