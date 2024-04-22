import random
from simple_term_menu import TerminalMenu


def main_menu():
    """
    Displays the main menu of the game.
    The user can choose between "Learn the rules", "Play the game", or "Exit".
    Depending on the user's choice, it triggers the appropriate actions.
    """
    options = ["Learn the rules", "Play the game", "Exit"]
    terminal_menu = TerminalMenu(options)
    while True:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Learn the rules":
            print_rules()
            go_back()
        elif options[menu_entry_index] == "Play the game":
            print("GAME")
            guess(20)  # Limit from 1 to 20 for the guessing game
            go_back()
        elif options[menu_entry_index] == "Exit":
            print("EXIT")
            exit()
        else:
            return


def go_back():
    """
    Allows the user to go back to the main menu from a sub-menu.
    """
    options = ["Go back to main menu"]
    go_back_menu = TerminalMenu(options)
    while True:
        menu_entry_index = go_back_menu.show()
        if menu_entry_index == 0:
            main_menu()


def guess(x):
    """
    Starts the number guessing game.
    
    Args:
        x (int): The upper limit for guessing the number.
    """
    random_number = random.randint(1, x)
    while True:
        user_input = input(f"Guess a number between 1 and {x}: ")
        if user_input.isdigit(): 
            guess = int(user_input)
            if 1 <= guess <= x:
                if guess < random_number:
                    print("Sorry, wrong number. Too low.")
                elif guess > random_number:
                    print("Sorry, guess again. Too high.")
                else:
                    print("Yay! You guessed it!")
                    break
            else:
                print(f"Please enter a number between 1 and {x}.")
        else:
            print("Please enter a valid number.")


def print_rules():
    """
    Displays the rules of the game.
    """
    print("RULES:")
    print("1. Choose a number between 1 and the specified limit.")
    print("2. Keep guessing until you find the correct number.")
    print("3. Enjoy the game and good luck!")


def main():
    """
    Main function of the program.
    Displays a welcome message and launches the main menu of the game.
    """
    print("Hey!")
    main_menu()


if __name__ == "__main__":
    main()
