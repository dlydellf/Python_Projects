# Python Course, Steps 315-317 ("File Transfer Submission", Pts. I, II & III)
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#------------------------------------
# Objective: Create a script that will transfer
#            files from one folder to another.
#------------------------------------

import shutil # imports the 'shutil' module
import os

# Sets the files' source path:
source = '/Users/Michell/Desktop/FolderA/'

# Sets the destination path (to FolderB):
destination = '/Users/Michell/Desktop/FolderB/'
files = os.listdir(source) # Retrieves ALL files currently within the 'source' directory

for i in files:
    shutil.move(source+i, destination) # Moves each file within the 'source' to its new destination
