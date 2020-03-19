import random
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view

# Initialise our views, all arguments are defaults
page_view = view.View()

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    return page_view("index")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    login = True
    
    if username != "admin": # Wrong Username
        err_str = "Incorrect Username"
        login = False
    
    if password != "password": # Wrong password
        err_str = "Incorrect Password"
        login = False
        
    if login: 
        return page_view("valid", name=username)
    else:
        return page_view("invalid", reason=err_str)
    
#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about_page():
    return page_view("about", garble=about_garble())

# Returns a random string each time
def about_garble():
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.", 
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from generation X and is on the runway heading towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------