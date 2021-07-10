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
#------------------------------------
'''
# Part 1:
import shutil # imports the 'shutil' module
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
#Part 2:
import shutil
import os

source = './SourceFolder/'
print(os.lstat(s))

#shutil.copy2(src, destination) # 'copy2' used here to attempt preserving files' metadata (creation/modification times, etc.)

