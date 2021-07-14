# Python Course, Steps 315-317 ("File Transfer Submission", Pts. I, II & III)
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#------------------------------------
# Objective: Part 1: Create a script that will transfer
#                    files from one folder to another.
#            Part 2: Create a script that 1) copies new files
#                    (and those edited within 24hrs) to a
#                    specific folder, and 2) transfers that
#                    folder's contents to ANOTHER folder.
#            Part 3: Encapsulate the functionality of Parts 1
#                    and 2 into a GUI.
#------------------------------------
'''
# Part 1:
import shutil
import os

# Sets the files' source path:
source = './FolderA/' # up one level (out of this .py file) and into the correct folder

# Sets the destination path (to FolderB):
destination = './FolderB/' # up one level (out of this .py file) and into the correct folder
files = os.listdir(source) # Retrieves ALL files currently within the 'source' directory
for i in files:
    shutil.move(source+i, destination) # Moves each file within the 'source' to its new destination
'''
#---------------
# Part 2:
import shutil # allows high-level file interactions (copying, removal, etc.)
import os
import datetime # importing the 'datetime' module instead of the 'time' module (thanks Hanna)

source = './Part2/New-Modified_Files_from_ALL_Users/' # the folder containing all of the day's .txt files (ONLY hardcoded as a default for Part2!!)
destination = './Part2/Destination_Folder(To_HomeOffice)/' # (this was also hardcoded only to use as a default within Part 2)

# This () iterates through ALL files in the source folder, creating an absolute path for ONLY the captured .txt files:
def captureTxtFiles(source='./Part2/New-Modified_Files_from_ALL_Users/'):    
    absoluteFilePaths = [] # An empty list to store each file's absolute file path
    allFiles = os.listdir(source) # '.listdir()' == the iterator
    textFiles = [files for files in allFiles if ".txt" in files] # --> isolating ONLY the .txt files
    for eachTxtFile in textFiles:
        absoluteFilePath = os.path.join(source, eachTxtFile) # an absolute file path is REQUIRED to determine lastModified's "modTime"!
        absoluteFilePaths.append(absoluteFilePath)
    lastModified(absoluteFilePaths, textFiles) # The next ()'s arguments...
        
# This () compares each .txt file's most recent modification time to the current time, copying those modified within the past 24hrs:
def lastModified(absoluteFilePaths, textFiles, destination='./Part2/Destination_Folder(To_HomeOffice)/'):
    timeNow = datetime.datetime.now().timestamp() # current time, in seconds
    time24hrsAgo = (timeNow-86400) # timeNow, minus a day's-worth of seconds (86,400)
    #print('Current time is {}'.format(timeNow))
    #print('  24hrs ago was {}'.format(time24hrsAgo))
    for eachFile in absoluteFilePaths:
        modTime = os.path.getmtime(eachFile) # when was each file last modified? (outputs in epoch/seconds)
        #print("{}\nLast Mod Timestamp: {}\n HASH Timestamp(?): {}\n".format(eachFile, modTime, hash(modTime)))
        if modTime <= time24hrsAgo:
            shutil.copy2(eachFile, destination) # using 'copy2' instead of 'copy' to attempt preserving files' metadata (creation/modification times, etc).
    print('textFiles={}'.format(textFiles))
    App.TxtFileResults(absoluteFilePaths, textFiles) # Captured .txt files (if any) cause updates to Part 3's GUI
    
'''
if __name__ == "__main__":
    captureTxtFiles()
'''
#-----------------
# Part 3:
import tkinter
from tkinter import * # Allows unpacking of ALL of tkinter's 'widgets' (tkinter CLASS objects)
from tkinter import filedialog as fd

class ParentWindow(Frame): # 'Frame' is the PARENT CLASS within tkinter
    def __init__(self, master): # 'self' == the ParentWindow class; 'masster' == the Frame class
        Frame.__init__(self)

        # The displayed window:
        self.master = master
        self.master.geometry('{}x{}'.format(880, 250)) # window's default size upon launching
        self.master.resizable(width=False, height=False) # User cannot resize window's x/y
        self.master.title('') # window's Title
        self.master.config(bg='lightgrey') # window's background color

        # The 'Select Folder' BUTTON:
        self.btn = Button(self.master, width=11, height=1, text="Select", command=self.directorySelect, font=('Helvetica, 10'))
        self.btn.grid(row=0, column=0, padx=(15,0), pady=(20,0), sticky=NW)

        # The 'Folder's Result' LABEL:
        self.Resultslbl = Label(self.master, width=90, text=('<<------  Use the "SELECT" button to choose which folder will be checked:'), font=('Helvetica, 10'))
        self.Resultslbl.grid(row=0, column=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=EW)

        # The '24hr Check' BUTTON:
        self.btnCheck = Button(self.master, width=11, height=2, text="24 Hours?", font=('Helvetica, 10'))
        self.btnCheck.grid(row=1, column=0, padx=(15,0), pady=(80,0), sticky=NW)

        # The 'Output Window' LABEL:
        self.Outputlbl = Label(self.master, width=45, text='', height=11, cursor='right_ptr')
        self.Outputlbl.grid(row=1, column=1, columnspan=2, padx=(20,0), pady=(10,0), sticky=NSEW)

    # To SELECT A DIRECTORY:
    def directorySelect(self):
        folder = fd.askdirectory() # The USER gets to decide within which folder to search for .txt files
        self.Resultslbl.config(text = "You've selected this folder path:\n{}".format(folder))
        captureTxtFiles('{}/'.format(folder)) # Chosen folder is passed into related function (above, in Part 2)
        if not folder: # If User closes dialog box or clicks the 'Cancel' button, return
            return

    # The Results of checking for .txt files:
    def TxtFileResults(self, absoluteFilePaths, textFiles):    
        if absoluteFilePaths == []:
            self.Outputlbl['text'] = "No text files were found in your chosen folder!\n\nPlease select a different folder."
        else:
            self.Resultslbl.config(text = "That folder contains these text files, which will be forwarded to the Home Office:")
            for eachFile in textFiles:
                self.Outputlbl['text'] += eachFile + '\n'

                #fileName = eachFile('\n')
                #self.Outputlbl.config(text = f'{fileName}')
        
            
if __name__ == '__main__':
    root = Tk() # 'Tk()' == tkinter's PARENT CLASS object, same as 'Frame') has been instantiated and named 'root'
    App = ParentWindow(root) # [(root -> Frame) -> passed into 'ParentWindow'] -> renamed 'App'
    root.mainloop() # prevents window from launching, then immediately closing
