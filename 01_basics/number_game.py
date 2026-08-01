"""
Guess The Number

A console-based guessing game with
multiple difficulty levels.

Features:
- Three difficulty levels
- Hot/Warm/Cold hints
- Input validation
- Replay option
"""

import random
import string



<<<<<<< HEAD
while True:

    while True:
        max_atttempts = 0
        difficulty = int(input("" \
        "1/ easy (1-50) 10 chance \n2/ hard (1-100) 8 chance \n3/ impossible (1-200) 6 chance: "))
        if difficulty in (1, 2, 3):
            if difficulty == 1:
                max_atttempts = 10
            elif difficulty == 2:
                max_atttempts = 8
            elif difficulty == 3:
                max_atttempts = 6
            break
        else:
            print("please insert a number in range 1 - 3")

    random_number = select_number(difficulty)
    won = False
    gussed = 0
    while gussed < max_atttempts:
        gussed += 1
=======
def choose_difficulty():
>>>>>>> 8af5a90 (add complete number guessing game)
        while True:
            number_guess = 0
            random_number = 0
            difficulty = (input("" \
            "1/ easy (1-50) 10 chance \n2/ hard (1-100) 8 chance \n3/ impossible (1-200) 6 chance: "))
            if difficulty.isdigit():
                difficulty = int(difficulty)
                if difficulty == 1:
                    return 10, random.randint(0, 50)
                elif difficulty == 2:
                    return 8, random.randint(0, 100)
                elif difficulty == 3:
                    return 6, random.randint(0, 200)
                else:
                    print("please insert a number in range 1 - 3")
            else:
                print("please insert a diggit")

def get_user_guess():
    while True:
        guesse = input("enter your guess: ")   
        if guesse.isdigit():
            guesse = int(guesse)
            return guesse
        else:
            print("insert a number")    


def play_game(repitition, number):   
    won = False
    counter = 0
    while counter < repitition:
        counter += 1
        user_guess = get_user_guess()
        if user_guess == random_number:
            print(f"you get it right at {counter} guess")
            won = True
            break
        elif abs(user_guess - random_number) < 5:
            print("it is burning")
        elif 5 <= abs(user_guess - random_number) < 15:
            print("you are close")
        elif 15 <= abs(user_guess - random_number) < 25:
            print("try harder")
        else: 
            print("not good")

    if not won:
         print("you lost")



while True:
    max_rep, random_number = choose_difficulty()
    print(max_rep, random_number)
    play_game(max_rep, random_number)
    play_again = input("do you wanna play again? (y/n)").strip().lower()
    if play_again == "n":
        break



<<<<<<< HEAD
    
=======







    
>>>>>>> 8af5a90 (add complete number guessing game)
