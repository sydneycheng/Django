# HTML info
# get request - database sends data to the application server (tanscribes into code)
# --> shows on the webpage

# post request - sends info to the database

# django is an all encompasing framework

#learning log
# models.py --> where we write code to create differnt "tables" (aka: objects) in our database



# DJANGO


## Starting our project
## the name of our project is learning_log --> it's important that we use a " ."

#django-admin startproject learning_log .
#this creates the "learning_log" folder as well as "manage.py"
#"manage.py" includes everything that makes our code run


## Create our database --> use MIGRATE command

#must use MIGRATE command everytime changes are made to our code
#python3 manage.py migrate
#this creates a database "db.sqlite3"
#sqlite is a database used for smaller development purposes
#on our local server


## We'll test our server by running it

#python3 manage.py runserver
#this downloads a default jango page (via a link)
#is a server on your local machine (rocket screen)
#the server continues running
#to Stop the server "ctrl + C"  --> if you try and refresh server, it will give an error


## Debugger: Instead of running this "runserver" command each time, use debugger

#click on "manage.py"
#go to debugger
#click "create a launch.json file"
