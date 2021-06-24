# listFiles() uses 'list comprehension', found at:
# https://www.w3schools.com/python/python_lists_comprehension.asp

import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') # The supplied tuple we're to work with

dbArgument1 = 'CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING)' # Creates the database table & its two columns

dbArgument2 = 'INSERT INTO tbl_files(col_fileName) VALUES (?)', \
        ('eachTextFile') # Should add all located '.txt' files to the database, >>>>> have NOT figured out how to add easch file according to its index yet <<<<<<

def dbMgmnt(dbArgument): # The standard template for manipulating our database's data; accepts custom database script arguments
    conn = sqlite3.connect('test.db') # Creates a 'test.db' database for use with sqlite3
    with conn:
        cur = conn.cursor() # The 'cursor' operates on the database
        cur.execute('{}'.format(dbArgument))
        conn.commit()
    conn.close()


def listFiles(fileList):
    textFiles = [files for files in fileList if '.txt' in files] # 'List comprehension': textFiles  = every file in fileList that meets the 'if' conditional
    for eachTextFile in textFiles:
        dbMgmnt(dbArgument2)


if __name__ == '__main__':
    dbMgmnt(dbArgument1)
    listFiles(fileList)

'''
This is supposed to follow this order:
1) dbMgmnt function is called, with "dbArgument1" as its argument,
    1.a - "tbl_files" is created
2) listFiles function is called, with "fileList" as its argument,
    2.a - both .txt files were found; already verified with a 'print(textFiles)' statement
HERE'S WHERE THE PROBLEM OCCURRED:
    2.b - For each .txt file found, I wanted the 'dbMgmnt' function to be called, with "dbArgument2' as its argument
    2.b.1 - That argument was SUPPOSED to insert the .txt file into the table, but isn't (see "Shell Screenshot" for the error code on line 20)
    2.b.2 - 'textFiles' IS a list [], but 'deMgmnt(dbArgument2)' is called for EACH file, so (?) no need to cycle through the list's indexes, right(?). I'm \
    thinking I should be able to add each individual file (denoted with "eachTextFile" on line 27) as 'dbMgmnt(dbArgument2) gets called, no problem.
Any thoughts/suggestions would be great
'''
