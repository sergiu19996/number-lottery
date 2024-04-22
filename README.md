# Number Guessing Game

A simple yet entertaining number guessing game implemented in Python. Test your guessing skills and see if you can guess the correct number within the specified range.


## How to Play

1. Run the program by executing the Python script.
2. Choose an option from the main menu:
    - Learn the rules: Read the rules of the game.
    - Play the game: Start guessing the number.
    - Exit: Quit the game.

: # (![screencapture-number-lottery-2-a0989c962984-herokuapp-2024-04-22-20_23_21](https://github.com/sergiu19996/number-lottery/assets/126587603/602e2130-bf85-416d-8745-2ef76af723c6)


3. If you choose to play the game, enter your guess when prompted.

: # (![screencapture-number-lottery-2-a0989c962984-herokuapp-2024-04-22-20_05_56](https://github.com/sergiu19996/number-lottery/assets/126587603/4857330f-07be-41d6-8b0b-10176b2dc0fe)


4. After each guess, the program will provide feedback.
![screencapture-number-lottery-2-a0989c962984-herokuapp-2024-04-22-20_06_04](https://github.com/sergiu19996/number-lottery/assets/126587603/b201992e-4fee-4262-8058-8757f1811c89)

   
5. Keep guessing until you correctly guess the number.
![screencapture-number-lottery-2-a0989c962984-herokuapp-2024-04-22-20_06_33](https://github.com/sergiu19996/number-lottery/assets/126587603/9e3f0f33-691c-4aed-b7d4-fd30e1daf57e)

   
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

## Application Performance

This application is designed to provide a smooth and seamless user experience. The interface is responsive, allowing users to navigate effortlessly through the menus. The interactions are intuitive, ensuring that users can quickly understand how to use the program without encountering any lag or delay.

Additionally, the application's performance has been optimized to ensure fast response times and minimal loading times. This means that users can enjoy a fluid experience, with no interruptions or slowdowns, even when running the program on lower-end devices or in resource-constrained environments.

For a visual representation of the application's performance, you can refer to the screenshot below, captured using Lighthouse:

![test light house](https://github.com/sergiu19996/number-lottery/assets/126587603/7c77b85f-dcec-4b8b-91c1-51d565c44287)
![screencapture-pep8ci-herokuapp-2024-04-22-20_05_20](https://github.com/sergiu19996/number-lottery/assets/126587603/e5ff59b2-08cb-4717-a1ed-f7a5c3dc95ae)

## Bugs

Here are some bugs that have been identified in the code:

1. **Input Validation Bug**: 
   - **Description**: When entering non-numeric input during the guessing game, the program does not handle the error gracefully.
   - **Impact**: This bug can cause the program to crash or produce unexpected behavior if the user enters invalid input.
   - **Fix**: Implement input validation to ensure that only numeric input is accepted during the guessing game.

2. **Infinite Loop Bug**:
   - **Description**: In certain scenarios, the program may enter an infinite loop and become unresponsive.
   - **Impact**: This bug prevents the user from interacting with the program and requires manually terminating the process.
   - **Fix**: Identify the conditions that lead to the infinite loop and implement appropriate exit conditions to prevent it.

3. **Display Bug**:
   - **Description**: The formatting of text output in the terminal may be inconsistent or unclear in some cases.
   - **Impact**: This bug can make it difficult for users to understand the information presented by the program.
   - **Fix**: Review the text formatting and ensure that it is consistent and easy to read across all scenarios.

4. **Compatibility Bug**:
   - **Description**: The program may not be compatible with certain versions of Python or external libraries.
   - **Impact**: This bug can prevent the program from running correctly on some systems or environments.
   - **Fix**: Update the code to ensure compatibility with a wider range of Python versions and dependencies.


  
## User Stories:
- First Time Visitor Goals:
  - Quickly understand the purpose of the program.
  - Navigate through the program easily.
  - Find the program useful and engaging.
- Frequent Visitor Goals:
  - Experience different outcomes by guessing different numbers.
  - Enjoy readable feedback and instructions.

## Acknowledgments

- This project was inspired by classic number guessing games.
- Special thanks to [simple-term-menu](https://github.com/IngoMeyer441/simple-term-menu) for providing an easy-to-use terminal menu library.


### Deploying to Heroku

To deploy the project to Heroku and run it as a remote web application, follow these steps:

1. Clone the repository:
git clone https://github.com/IuliiaKonovalova/madlib_with_python.git


2. Create your own GitHub repository to host the code.

3. Run the command `git remote set-url origin <(https://github.com/sergiu19996/number-lottery/tree/main)>` to set the remote repository location to your repository.

4. Push the files to your repository with the following command: 
git push

5. Create a Heroku account if you don't already have one [here](https://www.heroku.com/).

6. Create a new Heroku application [here](https://dashboard.heroku.com/new-app).

7. Link your GitHub account and connect the application to the repository you created.

8. Go to the Deploy tab and deploy the branch.

9. Wait for the completion of the deployment.

10. Click "Open app" to launch the application inside a web page.

### Deploying to Render

To deploy the project to Render and run it as a remote web application, follow these steps:

1. Link to the deployed application on Render: [number-lottery](<[Your Render App Link](https://number-lottery-2-a0989c962984.herokuapp.com/)>)

2. Create a new Render account if you don't already have one [here](https://render.com/).

3. Create a new application and choose Webserver.

4. Select the GitHub option and connect the application to the repository you created.

5. Search for the repository you created and click "Connect."

6. Create a name for the application and select the region where you want to deploy it.

7. Select the branch to deploy and choose the environment variables.

8. Set the Render build command to `pip3 install -r requirements.txt && npm install`.

9. Set the Render start command to `node index.js`.

10. Select the Free plan and click on "Advanced" settings.

11. Add the environment variables: 
 - `PORT` with the value `8000`
 - `PYTHON_VERSION` with the value `3.10.7`

12. Click "Create Web Service" and wait for the completion of the deployment.
