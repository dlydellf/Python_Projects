# Python_Projects
This repo stores The Tech Academy's Python projects, created using various modules such as tkinter and SQLite3
- Also included are *specific* examples of abstraction, encapsulation, inheritance, & polymorphism

## Projects:
- [Phonebook](https://github.com/dlydellf/Python_Projects/tree/main/Phonebook%20Assignment)
- [Database Submission](https://github.com/dlydellf/Python_Projects/tree/main/Database%20Submission%20Assignment%20(Step%20222))
- ["Check Files" GUI](https://github.com/dlydellf/Python_Projects/tree/main/File_Transfer_Submission_Assignment(Step_317))
- ["Webpage Generator"](https://github.com/dlydellf/Python_Projects/tree/main/Webpage_Generator_Submission_Assignment(Step_312))

### Phonebook
This CRUD project mimics a typical phonebook's functionality:
- Users can create (and save) a contact's name/phone number/email address in a database
- Previously stored entries can be read, updated, and/or deleted
 
### Database Submission
A code snippet, used as a precursor to the "Check Files" GUI:
- Its "listFiles" function has a dual role: 
  - Iterating through a supplied tuple for all .txt files, and...
  - Calling a database management function, passing in arguments after dynamically modifying them according to each files' specific location
- Its "database management" function then manipulates the database's data via two *custom* database strings

### "Check Files" GUI
This project allows a User to choose which .txt files are transferred from a chosen directory to another:
- Transferred files are then stored within a database
- The logic to transfer the chosen files is contained within the app's code
  - Comments throughout the app's code explain the transfer process

### "Webpage Generator"
This project is a tkinter-based GUI:
 - Users can input text they'd like displayed on their company's webpage
 - The webpage generation process is initiated within the app's code
   - Comments throughout the app's code explain how the webpage is generated
