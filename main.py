'''
Guess the secret number

The player needs to guess a number between 1 and 100.

'''
import random

def play_game():
    '''This function Runs the game'''
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input('Try a number between 1 and 100: '))
            except ValueError:
                print('❌ Only numbers allowed! Try again!')
                continue

            if guess < 1 or guess > 100:
                print('⚠️ Please, try a number between 1 and 100! ')
                continue

            attempts += 1

            if guess > secret_number:
                print('The secret number is lower!')
            elif guess < secret_number:
                print('The secret number is higher!')
            else:
                print(f'🎉 Congratulations! you did it with {attempts} attempts!')
                break
        play_again = input('Want to play again? (Yes/No): ').lower()
        if play_again != 'yes':
            print('👋 Thanks for playing!')
            break

play_game()
