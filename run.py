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
    elif capitalize_choice == "Tails":
        print("Tails it is")
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
        if computer_choice == 0:
            computer_selection = "Noughts"
            print(f"I think I'll pick {computer_selection}")
        elif computer_choice == 1:
            computer_selection = "Crosses"
            print(f"I'm going to pick {computer_selection}")
        else:
            print("Uh oh! Error!")
            coin_toss_outcome()
  

def new_game():
    welcome_message()
    coin_toss_choice()
#   coin_toss()
#   coin_toss_outcome()


coin_toss_outcome()

