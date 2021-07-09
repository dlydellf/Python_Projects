# Python Course - Steps 310 & 311 ("Webpage Generator", Pts 1 & 2)
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#------------------------------------
# Objective: Recreate a supplied GUI that allows users
#            to select a directory and show that directory
#            in a text field.
#------------------------------------
# line 43 == https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
#------------------------------------

import tkinter
from tkinter import * # Unpacks ALL of tkinter's 'wdigets' (tkinter CLASS objects)
import webbrowser # Module that displays web-based docs


# Main window's blueprint:
class ParentWindow(Frame): # 'Frame' == the PARENT CLASS within tkinter
    def __init__(self, master): # 'self' == the'ParentWindow' class; 'master' == the 'Frame' class
        Frame.__init__(self)

        # The displayed window:
        self.master = master
        self.master.geometry('{}x{}'.format(650, 260)) # Window's x/y
        self.master.resizable(width=False, height=False) # Internal widgets are ABSOLUTELY positioned, no need to resize window's x/y
        self.master.title('Webpage Generator, Pt.2')
        self.master.config(bg='lightgrey')

        # The LABEL:
        self.lbl = Label(self.master, text="Type your webpage's\n new content in the\n box to the right,\n\nthen...\n\nclick 'Submit' to update\nyour webpage with\nits new content!")
        self.lbl.place(x=5, y=5, width=140, height=220) # Uniform padding seperates widget from its neighbors
        
        # The TEXTBOX:
        # 'Text' == tkinter's MULTI-LINE textbox widget
        self.txtbx = Text(self.master, tabs=('.5c')) # Tabs shortened from 4cm to .5cm
        self.txtbx.place(x=150, y=5, width=495, height=250) # Textbox is ABSOLUTELY positioned, so RESIZABLE=FALSE
        
        # The SUBMIT Button:
        self.btn_Submit = Button(self.master, width=7, height=1, text="Submit", command=lambda: pageGenerator(self))
        self.btn_Submit.place(x=5, y=230, width=140)

# To generate webpage:
def pageGenerator(self):
    newContent = self.txtbx.get('1.0', 'end-1c') # Captures input within 'self.txtbx' 
    fileName = open("upcomingSale.html", "w") # if (!"upcomingSale") {create new file}; else {OVERWRITE existing content}
    fileName.write("<html>\n\t<body>\n\t\t<h1>\n\t{}\n\t\t</h1>\n\t</body>\n</html>".format(newContent)) # .txt file's HTML & new content
    fileName.close()
    webbrowser.open_new_tab('upcomingSale.html') # 'open_new_tab' does NOT require "http://" if only referencing a file!!
            
if __name__ == '__main__':
    root = Tk() # the object 'root' is created from the instantiated 'Tk()' (tkinter's PARENT CLASS)
    App = ParentWindow(root) # [(root === Frame) -> passed into 'ParentWindow'] -> assigned to 'App'
    root.mainloop() # Prevents window from launching, then immediately closing
