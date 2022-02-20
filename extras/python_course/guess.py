# This is a guess number game.
import random

def infoValidation(info):
    try:
        int(info)
        textType = 'int'
    except ValueError:
        try:
            float(info)
            textType = 'float'
        except ValueError:
            textType = 'str'
    return textType

# print('Hello. What is your name? ', end='')

while True:
    name = input('Hello. What is your name? ')
    if infoValidation(name) == 'str':
        break
    else:
        print('\tError: Please insert a valid name.')

    
secretNumber = random.randint(1, 20)
print('Well ' + name + ', I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 5):
# #    print('Take a guess: ', end='')
    
    while True:
        guess = input('Take a guess: ')
        if infoValidation(guess) == 'int':
            guess = int(guess)
            break
        else:
             print('\tError: Please insert a valid number.')
            
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:        
        break
    
if guess == secretNumber:
    print('You did it ' + name + '!' + ' You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, too much guesses, my number was:', secretNumber)


