import os
import time

filePath = 'C:\\Python_projects\\Step_213\\' # The folder being worked on

def listFiles(): # Part 2: This () iterates through a [] of ALL files within the above filePath:
    allFiles = os.listdir(filePath) # .listdir() --> does the iterating
    print("These are ALL the files within the '{}' folder: \n{}".format(filePath, allFiles))
    joinNameToPath(allFiles) # The output becomes joinNameToPath()'s argument

def joinNameToPath(allFiles): # Part 3: This () concatenates each file's name to the filePath, forming an absolute path:
    print("\nHere's a listing of their ABSOLUTE file paths: ")
    for fileName in allFiles:
        absolutePath = os.path.join(filePath, fileName) # .path.join --> does the concatenating
        print(absolutePath)
    getTime(allFiles) # The list of file names becomes getTime()'s arguments; the global filepath will be hardcoded

def getTime(allFiles): # Part 4: This () finds the most recent modification to each .TXT file:
    print("\nHere's a listing of when each TEXT file was last modified (local time): ")
    textFiles = [files for files in allFiles if ".TXT" in files]
    for eachTextFile in textFiles:
        absoluteFilePath = (filePath + eachTextFile)
        modificationTime = os.path.getmtime(absoluteFilePath) # .getmtime --> when was this path last modified (in seconds)?
        localTime = time.ctime(modificationTime) # .ctime --> changes the seconds into local time
        print("{}, last modified on {}".format(absoluteFilePath, localTime))

if __name__ == '__main__':
    listFiles()

