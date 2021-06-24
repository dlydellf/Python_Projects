# listFiles() uses 'list comprehension', found at:
# https://www.w3schools.com/python/python_lists_comprehension.asp

import sqlite3

# --------- The Setup: ---------
#   fileList:    the provided tuple for us to work on
#   dbArgument1:    creates the database (db) table & its two columns; 'ID' & 'col_fileName'
#   dbArgument2:    adds all located .txt files to the db
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
dbArgument1 = 'CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, col_fileName STRING)'
dbArgument2 = 'INSERT INTO tbl_files(col_fileName) VALUES (?,)'

 
# ----- The Functions: --------
#   dbMgmnt():   used twice to manipulate the db's data via the custom db scripts/strings/arguments 'dbArgument1' & 'dbArgument2'
#                   NOTE: 'supplement' is a PLACEHOLDER for the 'insert-these-values' portion of 'dbArgument2'
#                   (its default value = 'None', since 'dbArgument1' is a continuous string needing nothing concatenated to it)

def dbMgmnt(dbArgument, supplement = None):
    conn = sqlite3.connect('test.db') # Connects to the 'test.db' db
    with conn:
        cur = conn.cursor() # The 'cursor' operates on the db
        msg = '{}'.format(dbArgument), '("{}")'.format(supplement)
        print(msg)
        if msg.endswith(', ("None")'): # checks if 'dbAsrgument1' is the argument
            cur.execute('{}'.format(dbArgument))
        else:
            print("This is dbArgument2's print statement:\n{}".format(msg))
            cur.execute(msg)
        conn.commit()
    conn.close() # Vitally important to avoid dataleak


def listFiles(fileList):
    textFiles = [files for files in fileList if '.txt' in files] # 'List comprehension': textFiles  = every file in fileList that meets the 'if' conditional
    for eachTextFile in textFiles:
        dbMgmnt(dbArgument2, (eachTextFile))


if __name__ == '__main__':
    dbMgmnt(dbArgument1)
    listFiles(fileList)
