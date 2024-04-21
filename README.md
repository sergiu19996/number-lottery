# Number Guessing Game

A simple yet entertaining number guessing game implemented in Python. Test your guessing skills and see if you can guess the correct number within the specified range.


## How to Play:
1. Run the program by executing the Python script.
2. Choose an option from the main menu:
    - Learn the rules: Read the rules of the game.
    - Play the game: Start guessing the number.
    - Exit: Quit the game.
3. If you choose to play the game, enter your guess when prompted.
4. After each guess, the program will provide feedback.
5. Keep guessing until you correctly guess the number.
6. Have fun and enjoy the game!
 
## Features

- **Main Menu**: Choose from various options including learning the rules, playing the game, or exiting.
- **Rule Learning**: Understand the rules of the game before starting to play.
- **Interactive Gameplay**: Guess a number within the specified range and receive feedback on whether your guess is too high or too low.
- **Limit Customization**: Adjust the range of numbers to guess from for added challenge.
- **User-Friendly Interface**: Utilizes a terminal-based menu for easy navigation.
- **Restart Option**: Return to the main menu after playing a game to start over or explore other options.

- Technologies Used:
- Python 3.8.5
- Simple Terminal Menu
- Colorama (for adding colors to the terminal output)

## Installation

1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory.
3. Ensure you have Python installed on your system.
4. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Run the script using `python main.py`.
2. Navigate the main menu using the arrow keys or numeric keys and press Enter to select an option.
3. If you choose to play the game, enter your guesses when prompted.
4. Receive feedback on each guess and continue guessing until you find the correct number.
5. Return to the main menu to explore other options or play another round.


## Debugging

- **Invalid Input**: If you encounter errors related to invalid input, ensure that you are entering only numeric values when prompted for guesses.
- **Out of Range**: If you receive warnings about your guess being out of range, double-check the range specified and make sure your guess falls within it.
- **Endless Loop**: If the game seems to be stuck in an endless loop, check for logical errors in the code, especially within the guess evaluation loop.
  
## User Stories:
- First Time Visitor Goals:
  - Quickly understand the purpose of the program.
  - Navigate through the program easily.
  - Find the program useful and engaging.
- Frequent Visitor Goals:
  - Experience different outcomes by guessing different numbers.
  - Enjoy readable feedback and instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by classic number guessing games.
- Special thanks to [simple-term-menu](https://github.com/IngoMeyer441/simple-term-menu) for providing an easy-to-use terminal menu library.
