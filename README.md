# HOW TO INSTALL APP

`This app requires that python is installed on the system preferably python3.11.`

## INSTALLING VIRTUALENV

virtualenv is a python envirnment manangement library that isolate app from global python to install it

`python3 -m pip install virtualenv`

create a virtual environment

 `python3 -m virtualenv <name_of_environment>`

to activate virtual environment

`source <name_of_environment>/bin/python`

to install dependencies

`pip install -r requirements.txt` this will install the dependecies

setup the `.env` file and run:

`uvicorn app.main:app --reload --port <PORT>`
