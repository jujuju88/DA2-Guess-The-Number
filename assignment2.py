#import the random number generator
import random

#define a function to generate a random number
def random_number():
    global rand_nb
    rand_nb = random.randint(1,50)
    print(" Your number has been generated between 1 and 50.")

#generate a random number once and that is to be guessed
random_number()

#guessing the number with option of leaving with 'exit'
while True:
    guess_nb = input("Guess your number between 1 and 50: ")
    if guess_nb.isnumeric():
        guess_nb = int(guess_nb)
        if guess_nb > rand_nb:
            print("Your guess is too high.")
        elif guess_nb < rand_nb:
            print("Your guess is too low.")
        elif guess_nb == rand_nb:
            print("Congratulations! You guessed the number correctly. The number is", rand_nb, ".")
            break
    elif guess_nb == "exit":
        break
    else:
        print("It's not a number. Please enter a number.")
    
    
        

