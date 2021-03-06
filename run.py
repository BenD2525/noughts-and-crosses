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
next_free_row = len(results.get_values()) + 1
Analysis = SHEET.worksheet('Analysis')
multiple_games = False
chosen_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grid = [
        [chosen_slots[0], chosen_slots[1], chosen_slots[2]],
        [chosen_slots[3], chosen_slots[4], chosen_slots[5]],
        [chosen_slots[6], chosen_slots[7], chosen_slots[8]]
    ]
grid_positions = {'Player': [], 'Computer': []}

winning_combinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


def time_delay():
    """
    Sleeps the console for one second.
    """
    num_seconds = 1
    time.sleep(num_seconds)


def find_next_row():
    """
    Used to generate the next row on gspread
    when playing multiple rounds.
    """
    next_free_row = len(results.get_values()) + 1
    return next_free_row


def welcome_message():
    """
    Prints welcome message to user, explains the game
    and requests a username.
    """
    print("Welcome to Noughts and Crosses!")
    print("----------")
    time_delay()
    print("Also called 'Tic Tac Toe', try and beat me (your computer) ")
    print("by joining up to 3 noughts or crosses together before me!")
    time_delay()
    username = input("Now, who am I talking to? ")
    print(f"Pleased to meet you {username}.")
    time_delay()
    print("Nice to know the name of the person I'll beat!")
    time_delay()
    if multiple_games:
        results.update('A' + str(find_next_row()), username)
    else:
        results.update('A' + str(next_free_row), username)
    coin_toss_outcome()


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
        time_delay()
        print(f"It's {coin_toss_result}")
    elif result == 1:
        coin_toss_result = "Tails"
        print("The computer flicks the coin up...")
        time_delay()
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
        if multiple_games:
            results.update('B' + str(find_next_row() - 1), capitalize_choice)
        else:
            results.update('B' + str(next_free_row), capitalize_choice)
    elif capitalize_choice == "Tails":
        print("Tails it is")
        if multiple_games:
            results.update('B' + str(find_next_row() - 1), capitalize_choice)
        else:
            results.update('B' + str(next_free_row), capitalize_choice)
    else:
        print("You need to choose 'Heads' or 'Tails'. Let's try again.")
        coin_toss_choice()
    return capitalize_choice


def coin_toss_outcome():
    """
    Calculates who won the coin toss and prints a message for each
    result. If the user wins the coin toss, requests a choice of
    noughts or crosses and gives them the first turn.
    """
    capitalize_choice = coin_toss_choice()
    coin_toss_result = coin_toss()
    if capitalize_choice == coin_toss_result:
        print("You win- lucky guess...")
        time_delay()
        first_go = True
        sign_choice = input("Noughts or Crosses? \n")
        capitalize_sign = sign_choice.capitalize()
        if multiple_games:
            results.update('C' + str(find_next_row() - 1), coin_toss_result)
            results.update('D' + str(find_next_row() - 1), capitalize_sign)
        else:
            results.update('C' + str(next_free_row), coin_toss_result)
            results.update('D' + str(next_free_row), capitalize_sign)
        assign_sign_player(capitalize_sign, first_go)
        return first_go, capitalize_sign
    else:
        print("I win- binary is best!")
        time_delay()
        first_go = False
        computer_choice = random_number()
        if multiple_games:
            results.update('C' + str(find_next_row() - 1), coin_toss_result)
            results.update('D' + str(find_next_row() - 1), "-")
        else:
            results.update('C' + str(next_free_row), coin_toss_result)
            results.update('D' + str(next_free_row), "-")
        assign_sign_computer(computer_choice, first_go)
        return first_go, computer_choice


def assign_sign_player(capitalize_sign, first_go):
    """
    Takes player choice and assigns either noughts
    or crosses.
    """
    if capitalize_sign == "Noughts":
        print("You chose Noughts")
        player_sign = "O"
        computer_sign = "X"
    elif capitalize_sign == "Crosses":
        print("You chose Crosses")
        player_sign = "X"
        computer_sign = "O"
    else:
        print("You must choose 'Noughts' or 'Crosses'. Let's try again.")
        sign_choice = input("Noughts or Crosses? \n")
        capitalize_sign = sign_choice.capitalize()
    print(f"Player Sign: {player_sign}, Computer Sign: {computer_sign}")
    turn_order(first_go, player_sign, computer_sign)
    return player_sign, computer_sign, first_go


def assign_sign_computer(computer_choice, first_go):
    """
    Takes computer choice and assigns either noughts
    or crosses.
    """
    if computer_choice == 0:
        computer_selection = "Noughts"
        print(f"I think I'll pick {computer_selection}")
        computer_sign = "O"
        player_sign = "X"
    elif computer_choice == 1:
        computer_selection = "Crosses"
        print(f"I'm going to pick {computer_selection}")
        computer_sign = "X"
        player_sign = "O"
    else:
        print("Uh oh! Error!")
        coin_toss_outcome()
    print("----------")
    print(f"Player Sign: {player_sign}, Computer Sign: {computer_sign}")
    print("----------")
    turn_order(first_go, player_sign, computer_sign)
    return player_sign, computer_sign, first_go


def print_grid():
    """
    Prints grid using the chosen_slots list.
    """
    print("----------")
    for row in grid:
        for slot in row:
            print("|"f"{slot}", end="|")
        print()
    print("----------")


def check_user_choice(player_choice, computer_sign, player_sign):
    """
    Checks whether user choice for placement is already
    taken or not.
    """
    player_values = grid_positions.get('Player')
    if player_choice in player_values:
        print("You've already chosen it! Try again.")
        user_turn(player_sign, computer_sign)


def update_games():
    """
    Increments total game stat by 1 when called.
    """
    total_games = int(Analysis.get('D5').first())
    total_games += 1
    Analysis.update('D5', total_games)


def update_user_wins():
    """
    Increments user win stat by 1 when called.
    """
    user_wins = int(Analysis.get('D6').first())
    user_wins += 1
    Analysis.update('D6', user_wins)


def update_computer_wins():
    """
    Increments user win stat by 1 when called.
    """
    computer_wins = int(Analysis.get('D7').first())
    computer_wins += 1
    Analysis.update('D7', computer_wins)


def clear_scores():
    """
    Resets chosen slots and clears dictionary
    for a new game and returns an empty version.
    """
    global chosen_slots
    chosen_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global grid_positions
    grid_positions = {'Player': [], 'Computer': []}
    return chosen_slots, grid_positions


def check_if_win():
    """
    Checks if the user or the computer has won,
    if they have, it stops the game and displays a message.
    If not, continues the game.
    """
    player_stats = grid_positions.get('Player')
    computer_stats = grid_positions.get('Computer')
    for combo in winning_combinations:
        if all(num in player_stats for num in combo):
            print("You win!")
            update_user_wins()
            end_game()
        elif all(num in computer_stats for num in combo):
            print("I surprise myself sometimes. I win!")
            update_computer_wins()
            end_game()


def turn_order(first_go, player_sign, computer_sign):
    """
    Establishes whether user_turn or computer_turn
    is called first.
    """
    if first_go:
        user_turn(player_sign, computer_sign)
    else:
        computer_turn(computer_sign, player_sign)
    return player_sign, computer_sign


def exit_game():
    """
    Prints a goodbye message and exits the game.
    """
    print("Okay, goodbye friend!")
    quit()


def end_game():
    """
    Ends game and updates stats when called.
    """
    update_games()
    check_try_again()


def update_grid():
    """
    Updates grid with the relevant player_signs from the chosen_slots list.
    """
    global grid
    grid = [
        [chosen_slots[0], chosen_slots[1], chosen_slots[2]],
        [chosen_slots[3], chosen_slots[4], chosen_slots[5]],
        [chosen_slots[6], chosen_slots[7], chosen_slots[8]]
    ]
    return grid


def user_turn(player_sign, computer_sign):
    """
    Asks for user input for turn being taken. If a number greater than 9
    is input then error message is printed. Updates chosen_slots array
    and grid with player choice.
    """
    check_remaining_slots(chosen_slots)
    print("Press q to quit if you want to!")
    user_input = input(f"Pick any of {check_remaining_slots(chosen_slots)}\n")
    is_integer = user_input.isnumeric()
    if user_input == "q":
        exit_game()
    elif user_input != "q" and not is_integer:
        print("Please use a valid choice!")
        user_turn(player_sign, computer_sign)
    else:
        player_choice = int(user_input)
        try:
            if player_choice in check_remaining_slots(chosen_slots):
                check_user_choice(player_choice, computer_sign, player_sign)
                chosen_slots[player_choice - 1] = player_sign
                update_grid()
                grid_positions['Player'].append(player_choice)
                print_grid()
                check_if_win()
                computer_turn(computer_sign, player_sign)
                return chosen_slots, player_choice, grid_positions
            else:
                print("Please use a valid choice!")
                user_turn(player_sign, computer_sign)
        except ValueError:
            print("Please use a valid choice!")
            user_turn(player_sign, computer_sign)


def check_remaining_slots(chosen_slots):
    """
    Creates a list to select from when playing a turn.
    """
    updated_chosen_slots = []
    for slot in chosen_slots:
        if isinstance(slot, int):
            updated_chosen_slots.append(slot)
    if len(updated_chosen_slots) == 0:
        print("It's a draw!")
        end_game()

    return updated_chosen_slots


def is_next_game():
    """
    Changes multiple_games variable to True and returns value.
    Used for multiple round games.
    """
    global multiple_games
    multiple_games = True
    return multiple_games


def check_try_again():
    """
    Checks if user wants to try again. Starts another game,
    accesses data or exits game based on input.
    """
    choice = input("Would you like to try again?\n")
    lower_choice = choice.lower()
    if lower_choice == "yes":
        print("That's the spirit!")
        print("Let me do my spiel again :)")
        print("You can even change your name if you want!")
        print("----------")
        clear_scores()
        is_next_game()
        welcome_message()
    elif lower_choice == "no":
        data_choice = input("Would you like to see some stats?\n")
        data_choice_lower = data_choice.lower()
        if data_choice_lower == "yes":
            access_data()
        elif data_choice_lower == "no":
            exit_game()
        else:
            print("Yes or No only please, no fancy answers here!")
            check_try_again()
    else:
        print("Yes or No only please, no fancy answers here!")
        check_try_again()


def computer_turn(computer_sign, player_sign):
    """
    Uses a random number to generate a random choice for the computer.
    Checks whether the number has been used before, then updates the board
    with the computer's choice.
    """
    computer_choice = random.choice(check_remaining_slots(chosen_slots))
    print("My go- I think I'll go here...")
    chosen_slots[computer_choice - 1] = computer_sign
    grid_positions['Computer'].append(computer_choice)
    time_delay()
    update_grid()
    print_grid()
    check_if_win()
    user_turn(player_sign, computer_sign)
    return chosen_slots


def access_data():
    """
    Accesses the 'Analysis' tab in spreadsheet and prints
    detail to user.
    """
    print("Accessing database...")
    print("This might take a second!")
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
    print("----------")
    print("You have 3 choices: Games, Choices or Cancel")
    print("----------")
    request = input("What stats would you like to see?\n")
    capitalize_request = request.capitalize()
    if capitalize_request == "Games":
        print("Okay, let's have a look!")
        print("----------")
        print(f"You've played {total_games} games.")
        print("----------")
        time_delay()
        print(f"You've won {user_wins} times.")
        print(f"I've won {computer_wins} times.")
        print("----------")
        time_delay()
        print(f"You've got a {user_percentage}% win percentage.")
        print(f"I've got a {computer_percentage}% win percentage.")
        print("----------")
    elif capitalize_request == "Choices":
        print("Interested in your choices? Let me see!")
        print("Here we go:")
        print("----------")
        print(f"You've chosen heads {heads_choice} times.")
        print(f"This is {heads_choice_percentage}% of the time.")
        print("----------")
        time_delay()
        print(f"You've chosen tails {tails_choice} times.")
        print(f"This is {tails_choice_percentage}% of the time.")
        print("----------")
        time_delay()
        print(f"The coin landed on heads {heads_outcome} times.")
        print(f"This is {heads_outcome_percentage}% of the time.")
        print("----------")
        time_delay()
        print(f"The coin landed on tails {tails_outcome} times.")
        print(f"This is {tails_outcome_percentage}% of the time.")
        print("----------")
    elif capitalize_request == "Cancel":
        print("Okay")
        exit_game()
    else:
        print("You need to input one of the above!")
        access_data()
    user_choice = input("Anything else? Yes or No:\n")
    capitalize_choice = user_choice.capitalize()
    if capitalize_choice == "Yes":
        access_data()
    elif capitalize_choice == "No":
        exit_game()
    else:
        print("Yes or No only please, no fancy answers here!")
        access_data()


def new_game():
    """
    Initiates the first function and thus a new game.
    """
    welcome_message()


new_game()
