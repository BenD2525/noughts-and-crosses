import time
import random


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


def coin_toss():
    """
    Calculates a random number, 1 or 0, then assigns a 'heads'
    or 'tails' result based on the result. Prints a message to
    advise the user of the result.
    """
    result = round(random.randint(0, 1))
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


def coin_toss_choice():
    """
    Requests user input to choose heads or tails,
    validates their choice and prints it back to the user.
    Uses a random choice to select heads or tails, records result
    and displays a win or loss message
    """
    choice = input("Now, let's see who goes first. Heads or Tails? ")
    capitalize_choice = choice.capitalize()
    if capitalize_choice == "Heads":
        print("Heads it is")
        coin_toss()
    elif capitalize_choice == "Tails":
        print("Tails it is")
        coin_toss()
    else:
        print("You need to choose 'Heads' or 'Tails'. Let's try again.")
        coin_toss_choice()   
    print(capitalize_choice)


def coin_toss_outcome():
    """
    Calculates who won the coin toss and prints a message for each
    result.
    """
    if capitalize_choice == coin_toss_result:
        print("You win- lucky guess...")
    else:
        print("I win- binary is best!")
    

def new_game():
    welcome_message()
    coin_toss_choice()
    coin_toss()
    coin_toss_outcome()


new_game()