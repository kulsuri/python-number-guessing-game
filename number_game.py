#limit the number of guesses
#catch when user enters a non-integer
#print 'too high' or 'too low' for incorrect guesses
#let the user play again

import random

def validate_guess(guess):
    if guess.isdigit() == False:
        guess_is_an_int =  False
    else:
        guess_is_an_int = True
    return guess_is_an_int

def play_game_again():
    print("Would you like to play again... type YES or NO")
    play_again = input("> ").upper()
    if play_again == 'YES':
        main()
    elif play_again == 'NO':
        print("Bye")
        quit()
    else:
        print("What...?")
        play_game_again()

def main():
    secret_num = random.randint(1, 10)
    guesses = []
    print("Guess a number between 1 and 10...")

    while len(guesses) < 5:
        print("You have {} attempts remaining".format(5-len(guesses)))
        print("-------------------------------")

        guess = input("> ")
        guesses.append(guess)

        if validate_guess(guess) == True:
            guess = int(guess)

            if guess == secret_num:
                print("Correct! The number was {}".format(secret_num))
                break

            elif guess > secret_num:
                print("Too high!")

            elif guess < secret_num:
                print("Too Low!")
        else:
            print("{} is not a number!".format(guess))

    else:
        print("***** Bad luck! You ran out of attempts :( *******")
        print("The number was: {}. ".format(secret_num) + "Your guesses were: " + ", ".join(guesses))

    play_game_again()
    
main()
