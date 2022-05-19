import time


def welcome_message():
    """
    Prints welcome message to user, explains the game
    and requests a username.
    """
    num_seconds = 1
    print("Welcome to Noughts and Crosses!")
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
    Requests user input to choose heads or tails,
    validates their choice and prints it back to the user.
    Uses a random choice to select heads or tails, records result
    and displays a win or loss message
    """
    choice = input("Now, let's see who goes first. Heads or Tails? ")
    capitalize_choice = choice.capitalize()
    if capitalize_choice == "Heads":
        print("Heads it is")
    elif capitalize_choice == "Tails":
        print("Tails it is")
    else:
        print("You need to choose 'Heads' or 'Tails'. Let's try again.")
        coin_toss()    
    print(capitalize_choice)
    

def new_game():
    welcome_message()
    coin_toss()