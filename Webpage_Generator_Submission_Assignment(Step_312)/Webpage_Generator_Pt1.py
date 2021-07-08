# Python Course - Step 310 ("Webpage Generator", Pt1)
#   Created by: Douglas Foreman
#   Created using: Python/IDLE v3.9.4
#------------------------------------
# Objective: Recreate a supplied GUI that allows users
#            to select a directory and show that directory
#            in a text field.
#------------------------------------

import webbrowser # Module that displays web-based docs

# This script generates webpages:
def pageGenerator():
    fileName = open("upcomingSale.html", "w") # Create new .txt file, name "upcomingSale" (if it doesn't already exist); overwrite any existing content
    fileName.write("<html>\n\t<body>\n\t\t<h1>\n\tStay tuned for our amazing Summer sale!\n\t\t</h1>\n\t</body>\n</html>") # .txt file's HTML
    fileName.close()
    webbrowser.open_new_tab('upcomingSale.html') # does NOT require 'http://' if directing to a file
            
pageGenerator()
