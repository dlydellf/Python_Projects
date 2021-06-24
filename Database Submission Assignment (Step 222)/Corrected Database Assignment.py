# listFiles() uses 'list comprehension', found at:
# https://www.w3schools.com/python/python_lists_comprehension.asp

import sqlite3

# --------- The Setup: ---------
#   fileList:       the provided tuple for us to work on
#   dbArgument1:    creates the database (db) table & its two columns; 'ID' & 'col_fileName'
#   dbArgument2:    adds all located .txt files to the db
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
dbArgument1 = 'CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, col_fileName STRING)'
dbArgument2 = 'INSERT INTO tbl_files(col_fileName) VALUES ' # dbArgument2 needs two parameters that AREN'T seperated by a comma that is part of a string

 
# ----- The Functions: --------
#   dbMgmnt():   used twice to manipulate the db's data via the custom db scripts/strings/arguments 'dbArgument1' & 'dbArgument2'
#                   NOTE: 'supplement' is a PLACEHOLDER for the 'insert-these-values' portion of 'dbArgument2'
#                   (its default value = 'None', since 'dbArgument1' is a continuous string needing nothing concatenated to it)
#
#   listFiles():    used to: 1) iterate through the fileList tuple for all files ending with '.txt'
#                            2) call the dbMgmnt() with proper parameters for each .txt file found

def dbMgmnt(dbArgument, supplement = None):
    conn = sqlite3.connect('test.db') # Connects to the 'test.db' db
    with conn: # With an established connection...
        cur = conn.cursor() # 'conn.cursor()' allows manipulation of the db
        # msg = '{}'.format(dbArgument), '("{}")'.format(supplement)
        # if msg.endswith(', ("None")'): # checks if 'dbArgument1' is the argument
        if dbArgument == dbArgument1: # using this instead of the two lines above, since "AttributeError: 'tuple' object has no attribute 'endswith'"
            cur.execute('{}'.format(dbArgument))
        else:
            cur.execute('{}'.format(dbArgument) + '("{}")'.format(supplement))
        conn.commit()
    conn.close() # Important in avoiding dataleaks!


def listFiles(fileList):
    textFiles = [files for files in fileList if '.txt' in files] # Here's the "list comprehension"; textFiles  = every file in fileList that meets the 'if' conditional
    print('Here are the qualifying text files, legibly printed to your console:\n')
    for eachTextFile in textFiles:
        dbMgmnt(dbArgument2, (eachTextFile)) # FINALLY corrected the syntax to make this perform as expected by removing the "VALUES (?,)" portion :)
        print('{}'.format(eachTextFile))


if __name__ == '__main__':
    dbMgmnt(dbArgument1)
    listFiles(fileList)
