#Steps for update your VM once in AWS

## Setup the Initial Environment
	1. Update all the packages using sudo apt update. apt is the default package manager for linux
	2. install make, the latest python version and the package tree (for listing files in tree form) you can add any other packages you might find useful
	3. Once you've decided on the packages needed in the environment you can create a file called init.sh, the .sh stands for shell script, meaning it can be 
turned into a executable file using 'chmod +x init.sh' which adds a executable to the file format
	4. make sure to add a bash shebang at the top of the shell script so the linux knows to run the file as a bash script looks like this: '#!/bin/bash if you
haven't already then run 'bash init.sh' to execute the commands above

## Setup up GitUp

	1. Create a another shell script that documents your github user name and emails address, see seen below:
'#!/usr/bin/bash'

USER=<your github email>
NAME=<your github user name>

git config --global --list

git config --global user.email ${USER} 
git config --global user.name  ${NAME} 

git config --global --list

	2. Clone a repo if you have one already created
	3. Setup a remote, usually called origin
	4. push initial content to the main branch
	

## Create a Virtual Environment 

	1. Create a file call make file and include the content below, this will allow for stable environement to be created everytime you start the machine. 

default:
    @cat makefile

env:
    python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update:  env
    . env/bin/activate; pip install -r requirements.txt



	2. create the requirements.txt file and add the initial packages numpy and pandas 
	3. run the file by typing 'make update' this will execute the update command in the make file and load the packages in requirements.txt

	


