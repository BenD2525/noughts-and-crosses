import time
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Noughts and Crosses')

results = SHEET.worksheet('Results')
next_free_row = len(results.get_all_values()) + 1

chosen_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grid = [
        [chosen_slots[0], chosen_slots[1], chosen_slots[2]],
        [chosen_slots[3], chosen_slots[4], chosen_slots[5]],
        [chosen_slots[6], chosen_slots[7], chosen_slots[8]]
    ]


def welcome_message():
    """
    Prints welcome message to user, explains the game
    and requests a username.
    """
    print("Welcome to Noughts and Crosses!")
    num_seconds = 1
    time.sleep(num_seconds)
    print("Also called 'Tic Tac Toe', try and beat me (your computer) ")
    print("in a best of 5 games where the goal is to join")
    print("up to 3 noughts or crosses together before me!")
    num_seconds += 1
    time.sleep(num_seconds)
    username = input("Now, who am I talking to? ")
    print(f"Pleased to meet you {username}.")
    time.sleep(num_seconds)
    print("Nice to know the name of the person I'll beat!")
    time.sleep(num_seconds)
    results.update('A' + str(next_free_row), username)


def random_number():
    """
    Generates a random number (0 or 1) that is used to apply
    to other sections.
    """
    result = round(random.randint(0, 1))
    return result


def coin_toss():
    """
    Calculates a random number, 1 or 0, then assigns a 'heads'
    or 'tails' result based on the result. Prints a message to
    advise the user of the result.
    """
    result = random_number()
    if result == 0:
        coin_toss_result = "Heads"
        print("The computer flicks the coin up...")
        num_seconds = 1
        time.sleep(num_seconds)
        print(f"It's {coin_toss_result}")
    elif result == 1:
        coin_toss_result = "Tails"
        print("The computer flicks the coin up...")
        num_seconds = 1
        time.sleep(num_seconds)
        print(f"It's {coin_toss_result}")
    else:
        print("There's a glitch in the matrix, let's try again.")
    return coin_toss_result
  

def coin_toss_choice():
    """
    Requests user input to choose heads or tails,
    validates their choice and prints it back to the user.
    Uses a random choice to select heads or tails, records result
    and displays a win or loss message
    """
    choice = input("Now, let's see who goes first. Heads or Tails? \n")
    capitalize_choice = choice.capitalize()
    if capitalize_choice == "Heads":
        print("Heads it is")
        results.update('B' + str(next_free_row), capitalize_choice)
    elif capitalize_choice == "Tails":
        print("Tails it is")
        results.update('B' + str(next_free_row), capitalize_choice)
    else:
        print("You need to choose 'Heads' or 'Tails'. Let's try again.")
        coin_toss_choice()   
    return capitalize_choice


def coin_toss_outcome():
    """
    Calculates who won the coin toss and prints a message for each
    result. If the user wins the coin toss, requests a choice of
    noughts or crosses.
    """
    capitalize_choice = coin_toss_choice()
    coin_toss_result = coin_toss()
    if capitalize_choice == coin_toss_result:
        print("You win- lucky guess...")
        sign_choice = input("Noughts or Crosses? \n")
        capitalize_sign = sign_choice.capitalize()
        results.update('C' + str(next_free_row), coin_toss_result)
        results.update('D' + str(next_free_row), capitalize_sign)
        if capitalize_sign == "Noughts":
            print("You chose Noughts")
        elif capitalize_sign == "Crosses":
            print("You chose Crosses")
        else:
            print("You must choose 'Noughts' or 'Crosses'. Let's try again.")
            sign_choice = input("Noughts or Crosses? \n")
            capitalize_sign = sign_choice.capitalize()
    else:
        print("I win- binary is best!")
        computer_choice = random_number()
        results.update('C' + str(next_free_row), coin_toss_result)
        results.update('D' + str(next_free_row), "-")
        if computer_choice == 0:
            computer_selection = "Noughts"
            print(f"I think I'll pick {computer_selection}")
        elif computer_choice == 1:
            computer_selection = "Crosses"
            print(f"I'm going to pick {computer_selection}")
        else:
            print("Uh oh! Error!")
            coin_toss_outcome()
   

def print_grid(grid):
    """
    Prints grid using the chosen_slots list.
    """
    for row in grid:
        for slot in row:
            print("|"f"{slot}", end="|")
        print()


def user_turn():
    """
    Asks for user input for turn being taken. If a number greater than 9
    is input then error message is printed. Updates chosen_slots array
    and grid with player choice.
    """
    user_input = input("Make your move.. Choose between slots 1-9\n")
    player_choice = int(user_input)
    if player_choice <= 9 and player_choice != 0:
        chosen_slots.remove(player_choice)
        chosen_slots.insert(player_choice - 1, "x")
        print(chosen_slots)
        print_grid(grid)
    else:
        print("Please select a number between 1 and 9.")
        user_turn()


def computer_turn():
    """
    Uses a random number to generate a random choice for the computer.
    """
    computer_choice = round(random.randint(1, 9))
    print("My go- I think I'll go here...")
    chosen_slots.remove(computer_choice)
    chosen_slots.insert(computer_choice - 1, "x")
    print(chosen_slots)
    print_grid(grid)
  

def access_data():
    """
    Accesses the 'Analysis' tab in spreadsheet and prints
    detail to user.
    """
    print("Accessing database...")
    print("Bear with me!")
    Analysis = SHEET.worksheet('Analysis')
    total_games = Analysis.get('D5').first()
    user_wins = Analysis.get('D6').first()
    computer_wins = Analysis.get('D7').first()
    user_percentage = Analysis.get('D8').first()
    computer_percentage = Analysis.get('D9').first()
    heads_choice = Analysis.get('G5').first()
    tails_choice = Analysis.get('G6').first()
    heads_choice_percentage = Analysis.get('G7').first()
    tails_choice_percentage = Analysis.get('G8').first()
    heads_outcome = Analysis.get('J5').first()
    tails_outcome = Analysis.get('J6').first()
    heads_outcome_percentage = Analysis.get('J7').first()
    tails_outcome_percentage = Analysis.get('J8').first()

    print("You have 3 choices: Games, Choices or Cancel")
    request = input("What stats would you like to see?\n") 
    capitalize_request = request.capitalize()
    if capitalize_request == "Games":
        print("Okay, let's have a look!")
        print(f"You've played {total_games} games.")
        print(f"You've won {user_wins} times.")
        print(f"I've won {computer_wins} times.")
        print(f"You've got a {user_percentage}% win percentage.")
        print(f"I've got a {computer_percentage}% win percentage.")
    elif capitalize_request == "Choices":
        print("Interested in your choices? Let me see!")
        print("Here we go:")
        print(f"You've chosen heads {heads_choice} times.")
        print(f"This is {heads_choice_percentage}% of the time.")
        print(f"You've chosen tails {tails_choice} times.")
        print(f"This is {tails_choice_percentage}% of the time.")
        print(f"The coin landed on heads {heads_outcome} times.")
        print(f"This is {heads_outcome_percentage}% of the time.")
        print(f"The coin landed on tails {tails_outcome} times.")
        print(f"This is {tails_outcome_percentage}% of the time.")
    elif capitalize_request == "Cancel":
        print("Okay")
        return
    user_choice = input("Anything else? Yes or No:\n")
    capitalize_choice = user_choice.capitalize()
    if capitalize_choice == "Yes":
        access_data()
       

def new_game():
    """
    Initiates the game and contains other functions.
    """
    welcome_message()
    coin_toss_outcome()
    user_turn()
    computer_turn()


access_data()