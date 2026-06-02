#!/usr/bin/bash

USER=bwright.wright6@gmail.com
NAME=NovaVolunteer

git config --global --list

git config --global user.email ${USER} 
git config --global user.name  ${NAME} 

git config --global --list
