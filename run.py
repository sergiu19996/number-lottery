from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/play')
def play():
    return render_template('game.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    random_number = random.randint(1, 20)
    if guess == random_number:
        return "Congratulations! You guessed the correct number!"
    elif guess < random_number:
        return "Sorry, your guess is too low. Try again!"
    else:
        return "Sorry, your guess is too high. Try again!"

if __name__ == '__main__':
    app.run(debug=True)