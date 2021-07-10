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

here = './Part2/(start)New_and_Modified_Files_from_ALL_Users/' # the folder containing all of the day's .txt files...

# This () iterates through ALL files in above folder, returning only the .txt files after creating an absolute path to each file:
def captureTxtFiles():
    allFiles = os.listdir(here) # '.listdir()' == the iterator
    textFiles = [files for files in allFiles if ".txt" in files] # --> isolating ONLY the .txt files
    for eachTxtFile in textFiles:
        absoluteFilePath = (here + eachTxtFile) # Concatenates each .txt fileName & filePath into an absolute path
    within24Hrs(textFiles) # The output becomes the next ()'s argument

# This () compares each .txt files' most recent modification to the current time:
def within24Hrs(textFiles):    
        modTime = os.path.getmtime(absoluteFilePath) # when was the file last modified (in epoch/seconds)?
        localTime = datetime(modTime) # changes 'modTime' into the local time
        hour = time.localtime(modTime).tm_hour # 'localtime(epoch).tm_hr' == returns the hour (in military time)
        date = time.localtime(modTime).tm_mday
        print("{}\n\t{} <<>> hr/dy: {} <<>> day/mnth:{}".format(absoluteFilePath, localTime, hour, date))
        print(time.ctime())
        #if hour < 24:
            
        


if __name__ == "__main__":
    captureTxtFiles()


#shutil.copy2(src, destination) # 'copy2' used here to attempt preserving files' metadata (creation/modification times, etc.)

