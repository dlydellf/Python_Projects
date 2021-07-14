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
#--------
# Part 2:
#--------
import shutil # allows high-level file interactions (copying, removal, etc.)
import os
import datetime # importing the 'datetime' module instead of the 'time' module (thanks Hanna)

source = './Part2/New-Modified_Files_from_ALL_Users/' # the folder containing all of the day's .txt files (ONLY hardcoded as a default for Part2!!)
destination = './Part2/Destination_Folder(To_HomeOffice)/' # (this was also hardcoded only to use as a default within Part 2)



# Step 2 - Iterate through ALL files in the source folder, creating an absolute path for ONLY any captured .txt files:
def captureTxtFiles(source='./Part2/New-Modified_Files_from_ALL_Users/'):    
    absolFilePaths = [] # An empty list to store each file's absolute file path
    allFiles = os.listdir(source) # '.listdir()' == the iterator
    textFiles = [files for files in allFiles if ".txt" in files] # --> isolating ONLY the .txt files
    for eachTxtFile in textFiles:
        absolFilePath = os.path.join(source, eachTxtFile) # an absolute file path is REQUIRED to determine lastModified's "modTime"!
        absolFilePaths.append(absolFilePath)
    App.TxtFileResults(absolFilePaths, textFiles) # Step 3, bottom
    
        
# Step 5 - Compares each .txt file's most recent modification time to the current time, copying those modified within the past 24hrs:
def lastModified(self):
    timeNow = datetime.datetime.now() # current time, in seconds
    time24hrsAgo = timeNow - datetime.timedelta(hours=24)
    absoluteFilePaths = os.listdir(self.sourcefolder)
    print(self.sourcefolder)
    print(absoluteFilePaths)
    for eachFile in absoluteFilePaths:
        modTime = os.path.getmtime(self.sourcefolder+'/'+eachFile) # when was each file last modified? (functional, thanks to Levi!!)
        modificationTime = datetime.datetime.fromtimestamp(modTime)
        if modificationTime >= time24hrsAgo:
            shutil.copy2(self.sourcefolder+'/'+eachFile, self.destinationfolder) # using 'copy2' instead of 'copy' to attempt preserving files' metadata (creation/modification times, etc).
    App.OutputWindow['text'] = "All text files within the chosen\nfolder have been successfully copied to\nyour destination folder" # Captured .txt files (if any) cause updates to Part 3's GUI
    
'''
if __name__ == "__main__":
    captureTxtFiles()
'''
#--------
# Part 3:
#--------
import tkinter
from tkinter import * # Allows unpacking of ALL of tkinter's 'widgets' (tkinter CLASS objects)
from tkinter import filedialog as fd

class ParentWindow(Frame): # 'Frame' is the PARENT CLASS within tkinter
    def __init__(self, master): # 'self' == the ParentWindow class; 'masster' == the Frame class
        Frame.__init__(self)

#------------------------
#   The displayed window:
#------------------------
        self.master = master
        self.master.geometry('{}x{}'.format(880, 450)) # window's default size upon launching
        self.master.resizable(width=False, height=False) # User cannot resize window's x/y
        self.master.title('') # window's Title
        self.master.config(bg='lightgrey') # window's background color
        self.sourcepath = ""
        self.destinationpath=""

        # The 'Select Folder' BUTTON:
        self.btn = Button(self.master, width=11, height=1, text="Source", command=self.directorySelect, font=('Helvetica, 10'))
        self.btn.grid(row=0, column=0, padx=(15,0), pady=(20,0), sticky=NW)

        # The 'Folder's Result' LABEL:
        self.Resultslbl = Label(self.master, width=90, wraplength=650, text=('<<------  Use the "SOURCE" button to choose which folder will be checked:'), font=('Helvetica, 10'))
        self.Resultslbl.grid(row=0, column=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=EW)

        # The 'File Check' BUTTON:
        self.fileCheck = Button(self.master, width=11, height=2, text="No Files\nTo check", font=('Helvetica, 10'))
        self.fileCheck.grid(row=2, column=0, padx=(15,0), pady=(180,0), sticky=NW)

        # The 'Output Window' LABEL:
        self.OutputWindow = Label(self.master, width=45, wraplength=650, text='', height=25, cursor='right_ptr')
        self.OutputWindow.grid(row=2, column=1, columnspan=2, padx=(20,0), pady=(5,0), sticky=NSEW)

#----------------
#   The FUNCTIONS
#----------------

    # Steps 1 & 4 - Select 'SOURCE' & 'DESTINATION' directories:
    def directorySelect(self, *args):
        folder = fd.askdirectory() # Allows User to decide which folders are selected
        if not folder: # if User closes dialog box or clicks the 'Cancel' button, return
            return
        elif "RECEIVING" in self.Resultslbl['text']:
            self.OutputWindow['text'] = "You've selected this folder's path as the DESTINATION:\n{}\n\n<<--------------------------\n\nUse the 'Initiate FileCheck Now?' button\nto begin the file check process...".format(folder)
            self.Resultslbl['text'] = 'The "Initate FileCheck Now?" button has become available...'
            self.fileCheck['text'] = "Initiate\nFileCheck now?"
            self.destinationfolder = folder
            self.fileCheck['command'] = lastModified(self) ######## either this function 1) is missing its 2 arguments (when using "*args"), or 2) the arguments aren't defined (when I explicitely state them, like I'm doing here)
            lastModified(self) # all 3 arguments passed into Step 5 (above, in Part 2)...
        else:
            self.OutputWindow['text'] = "You've selected this folder's path as the SOURCE:\n{}".format(folder)
            self.sourcefolder = folder
            captureTxtFiles(folder) # Chosen folder is passed into Step 2 (above, in Part 2), replacing the default 'source'   
            
            
    # Step 3 - Did the folder contain any .txt files?
    def TxtFileResults(self, absolFilePaths, textFiles):    
        if absolFilePaths == []: # there are no .txt files in the chosen folder
            self.Resultslbl['text'] = "Your chosen folder contains no text files;\nPlease select a different folder"
            self.directorySelect # back to Step 1...
        else:
            self.OutputWindow['text'] += "\n\nThese are the text files within your SOURCE folder:\n"
            for eachFile in textFiles:
                self.OutputWindow['text'] += eachFile + '\n'
            self.btn['text'] = 'Destination' # Reassigning previous element; User is prompted to Step 1 (now Step 4)
            self.Resultslbl['text'] = '<<<-----  The folder RECEIVING these files can now be selected with the "DESTINATION" button'
            #self.directorySelect(self, absoluteFilePaths, textFiles)
            

            
if __name__ == '__main__':
    root = Tk() # 'Tk()' == tkinter's PARENT CLASS object, same as 'Frame') has been instantiated and named 'root'
    App = ParentWindow(root) # [(root -> Frame) -> passed into 'ParentWindow'] -> renamed 'App'
    root.mainloop() # prevents window from launching, then immediately closing
