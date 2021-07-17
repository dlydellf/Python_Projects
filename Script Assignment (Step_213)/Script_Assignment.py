# Python Course, Step 213 ("Script Assignment")
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
# ------------------------------------
# Objectives:
#   A) Use the 'listdir()' method to iterate through all files within a specific directory;
#   B) Use the 'path.join()' method to create an absolute file path (by concatenating each file's name to its path);
#   C) Use the 'getmtime()' method to find the latest date each file was created/modified;
#   D) Print each file that ends with a '.txt' extension (and its corresponding mtime) to the console.
# ------------------------------------
import os
import time

filePath = 'C:\\Python_projects\\Step_213\\'  # The folder being worked on


# Objective A - Iterating through a [] of ALL files within the above filePath:
def listFiles():
    allFiles = os.listdir(filePath)  # '.listdir()' --> does the iterating
    print("These are ALL the files within the '{}' folder: \n{}".format(
        filePath, allFiles))
    joinNameToPath(allFiles)  # The output becomes joinNameToPath()'s argument


# Objective B - Concatenating each file's name to its filePath, creating an absolute path:
def joinNameToPath(allFiles):
    print("\nHere's a listing of their ABSOLUTE file paths: ")
    for fileName in allFiles:
        # '.path.join()' --> does the concatenating
        absolutePath = os.path.join(filePath, fileName)
        print(absolutePath)
    # The list of file names becomes getTime()'s arguments; the global filepath will be hardcoded
    getTime(allFiles)


# Objective C - Finding the most recent modification to each .TXT file:
def getTime(allFiles):
    print("\nHere's a listing of when each TEXT file was last modified (local time): ")
    textFiles = [files for files in allFiles if ".TXT" in files]
    for eachTextFile in textFiles:
        absoluteFilePath = (filePath + eachTextFile)
        # '.getmtime()' --> when was this path last modified (in epoch/seconds)?
        modificationTime = os.path.getmtime(absoluteFilePath)
        # '.ctime()' --> changes the epoch/seconds into local time
        localTime = time.ctime(modificationTime)
        # Objective D - Printing each file ending with a '.txt' & its mtime to console:
        print("{}, last modified on {}".format(absoluteFilePath, localTime))


if __name__ == '__main__':
    listFiles()
