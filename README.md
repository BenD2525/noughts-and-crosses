# Noughts and Crosses
Noughts and Crosses is a Python terminal game which runs in Heroku.

Users can log a username, take part in a coin toss and play as many games of Noughts and Crosses (also known as Tic Tac Toe) as they want. Their username, coin toss choice, coin toss result, choice of Noughts or Crosses and game results are logged to an external spreadsheet. This can be accessed after playing a game if the user would like to know what their stats are.

LINK TO DEPLOYED PROJECT

## How to Play
Noughts and Crosses is a classic game that can be played across many forms.

This program requests a username from the user which is then logged on the external spreadsheet. There is then a coin toss which is determined by a random number. Depending on the coin toss outcome, the user then chooses either noughts or crosses.

The game then begins and the user selects the slots they wish to choose, aiming to get a chain of three of the same sign. The user takes turns with the computer. Once a winner or a draw is confirmed, the program will ask if the user wishes to try again. If the user selects yes, the program will play again. If not, the user can access data from the external spreadsheet which has been updated with stats from the game.

## Features

### Existing Features
- Welcome message
- Random coin toss generation
- Printing of board with updated X and O choices
- Determination of winner or draw
- Ability to play more than once
- Input validation for each input request
- Storing of username, coin toss choice/result and game results.
- Access to the above information when the user requests it.

### Future Features
- Add colours to computer/user selections on board

## Data Structure
I used a dictionary as my data structure for this game. 

The dictionary begins empty and logs each of the user and computer's moves. The moves are selected using the keys 1-9, and if a slot has been taken it is removed from selection for the player on the next turn.

In order to calculate the result of the game during both the computer and user turns, the check_if_win function compares the current 'Player' and 'Computer' key values against the list of winning combinations stored in global scope. If there is a match, the relevant win message and subsequent functions are stored.

If there are no available slots and there is no winner, the game will be counted as a draw.

## Testing
I have tested this project by doing the following:

- Passed the code through PEP8 and confirmed that there were no problems
- Tested input validation (tried input which wasn't requested by the program) and confirmed that no errors were thrown
- Tested in my local terminal and on Heroku

## Bugs
### Solved Bugs

- When testing the project, I found that the data was being stored incorrectly on the second game. To solve this I created a new variable, multiple_games, which starts as False and becomes True when starting a second game. Based on this, there are if statements which ensure that a new row is populated on the spreadsheet.
- The grid wasn't printing an updated version on each turn, just the starting version. I created a separate function, update_grid, to fix this.
- The exit_game function was not correctly exiting the game and was allowing the game loop to continue after the function had been called, so I added quit() to the function.

### Remaining Bugs
- No bugs remaining

### Validator Testing
- No errors were return from PEP8

## Deployment
This project was deployed using Code Institute's mcok terminal for Heroku.

Stephs to deploy:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits
- Code Institute for the deployment terminal
- W3 schools for clarifying my understanding on Python Dictionaries