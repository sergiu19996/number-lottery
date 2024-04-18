import random
from simple_term_menu import TerminalMenu


def main_menu():
    options = ["Learn the rules", "Play the game", "Exit"]
    terminal_menu = TerminalMenu(options)
    while True:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Learn the rules":
            print_rules()
            go_back()
        elif options[menu_entry_index] == "Play the game":
            print("GAME")
            guess(20)  # Limita de la 1 la 20 pentru jocul de ghicit
            go_back()
        elif options[menu_entry_index] == "Exit":
            print("EXIT")
            exit()
        else:
            return


def go_back():
    options = ["Go back to main menu"]
    go_back_menu = TerminalMenu(options)
    while True:
        menu_entry_index = go_back_menu.show()
        if menu_entry_index == 0:
            main_menu()


def guess(x):
    random_number = random.randint(1, x)
    while True:
        user_input = input(f"Guess a number between 1 and {x}: ")
        if user_input.isdigit():  # Verifică dacă intrarea este formată din cifre
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
    print("RULES:")
    print("1. Try to guess the correct number between 1 and the specified limit.")
    print("2. After each guess, you will be told if the actual number is higher or lower.")
    print("3. Keep guessing until you find the correct number.")
    print("4. Have fun and enjoy the game!")


def main():
    print("Hey!")
    main_menu()


if __name__ == "__main__":
    main()