
i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)

# exercise

print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  ->
#2. What do I want to change each time?
#  ->
#3. How long should we repeat?
#  ->

num = 56
guess = 0
guess_limit = 5
guess_number = 0
guess = int(input(f'Guess a number between 1 and 100: '))
guess_number += 1
while guess_number < guess_limit:
    if guess != num:
        guess_number += 1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} Too low - Guess again 1-100: '))
    if guess == num:
        print(f'Awesome!!! Number {guess} is the correct guess')
        break

if guess != num:
    print(f'Sorry you lost! It was {num}')
