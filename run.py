from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if 'random_number' not in session:
        # Generate a random number if not already in the session
        session['random_number'] = random.randint(1, 20)
    
    random_number = session['random_number']

    if guess == random_number:
        # If the number is correctly guessed, remove the random number from the session
        session.pop('random_number', None)
        return "Congratulations! You guessed the correct number!"
    elif guess < random_number:
        return "Sorry, your guess is too low. Try again!"
    else:
        return "Sorry, your guess is too high. Try again!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))