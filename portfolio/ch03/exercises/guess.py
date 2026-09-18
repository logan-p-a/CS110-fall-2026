import random

randInt = random.randint(1,10)
guess1 = int(input("Guess a number between 1 and 10: "))
if guess1 != randInt:
    if guess1 < randInt:
        print("Too low!")
    else:
        print("Too high!")
    guess2 = int(input("Guess again: "))
    if guess2 != randInt:
        if guess2 < randInt:
            print("Too low!")
        else:
            print("Too high!")
        guess3 = int(input("Guess again: "))
        if guess3 != randInt:
            if guess3 < randInt:
                print("Too low!")
            else:
                print("Too high!")
            print("Sorry, the number was", randInt)
        else:
            print("You guessed it!")
else:
    print("You guessed it!")
