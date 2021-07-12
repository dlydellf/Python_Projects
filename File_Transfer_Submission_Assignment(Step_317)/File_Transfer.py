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
#Part 2:
import shutil
import os
import datetime # importing the 'datetime' module instead of the 'time' module (thanks Hanna)

source = './Part2/New-Modified_Files_from_ALL_Users/' # the folder containing all of the day's .txt files...
destination = './Part2/Destination_Folder(To_HomeOffice)/'

# This () iterates through ALL files in the source folder, creating an asolute path for ONLY the captured .txt files:
def captureTxtFiles():    
    absoluteFilePaths = [] # An empty list to store each file's absolute file path
    allFiles = os.listdir(source) # '.listdir()' == the iterator
    textFiles = [files for files in allFiles if ".txt" in files] # --> isolating ONLY the .txt files
    for eachTxtFile in textFiles:
        absoluteFilePath = os.path.join(source, eachTxtFile) # an absolute file path is REQUIRED to use Line 52's 'os.path.getmtime'!!
        absoluteFilePaths.append(absoluteFilePath)
    lastModified(absoluteFilePaths) # Output becomes the next ()'s argument

# This () compares each .txt file's most recent modification time to the current time, copying those modified within the past 24hrs:
def lastModified(absoluteFilePaths):
    timeNow = datetime.datetime.now().timestamp() # current time, in seconds
    time24hrsAgo = (timeNow-86400) # timeNow, minus a day's-worth of seconds (86,400)
    #print('Current time is {}'.format(timeNow))
    #print('  24hrs ago was {}'.format(time24hrsAgo))
    for eachFile in absoluteFilePaths:
        modTime = os.path.getmtime(eachFile) # when was each file last modified? (outputs in epoch/seconds)
        #print("{}\nLast Mod Timestamp: {}\n HASH Timestamp(?): {}\n".format(eachFile, modTime, hash(modTime)))
        if modTime >= time24hrsAgo:
            shutil.copy2(eachFile, destination) # using 'copy2' instead of 'copy' to attempt preserving files' metadata (creation/modification times, etc).
    print(os.listdir(destination))         

if __name__ == "__main__":
    captureTxtFiles()
