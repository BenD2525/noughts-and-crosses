# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to Noughts and Crosses!")
username = input("Please tell me your name: ")
print(f"Pleased to meet you {username}.")


def coin_toss():
    choice = input("Let's see who goes first. Heads or Tails? ")
    capitalize_choice = choice.capitalize()
    if capitalize_choice == "Heads":
        print("Heads it is")
    elif capitalize_choice == "Tails":
        print("Tails it is")
    else:
        print("You need to choose 'Heads' or 'Tails'. Let's try again.")
        
    print(capitalize_choice)
    coin_toss()


coin_toss()