#! /bin/bash

## TESTED: 07/07/2026
## TESTED BY: Wahab
## TESTED ON: AWS
## AIM: Work as a script + user data on an instance created with a TicTacToe AMI
## Purpose: Connects the TicTacToe app to the MongoDB and starts the app
## PREREQUISITE: Change the IP before using as a script or user data

cd /tech610-tic-tac-toe/app

echo Creating environment variable to connect to MongoDB...
export MONGODB_URI=mongodb://ENTER IP HERE:27017/tictactoe
echo Created MONGODB_URI environment variable.

echo Starting app...
pm2 start index.js
echo Application has started!

