from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key'


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    message_type = ''

    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['game_over'] = False

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'restart':
            session['secret_number'] = random.randint(1, 100)
            session['attempts'] = 0
            session['game_over'] = False

        else:
            guess = int(request.form['player_guess'])
            session['attempts'] += 1
            secret_number = session['secret_number']

            if guess > secret_number:
                message = 'The Guess is too high!'
                message_type = 'too-high'
            elif guess < secret_number:
                message = 'The Guess it too low!'
                message_type = 'too-low'
            else:
                attempts = session['attempts']
                message = f"Congratulations! You guessed it in {attempts} attempts!"
                message_type = 'success'

                session['game_over'] = True

    return render_template('index.html', message=message, message_type=message_type, game_over=session['game_over'])


if __name__ == '__main__':
    app.run(debug=True)
