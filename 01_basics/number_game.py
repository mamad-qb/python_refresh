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

def select_number(level):
    number = 0
    if level == 1:
        number = random.randint(0, 50)
    if level == 2:
        number = random.randint(0, 100)
    if level == 3:
        number = random.randint(0, 200)
    return number


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
        while True:
            user_input = input("Enter your guess: ")
            if user_input.isdigit():
                user_input = int(user_input)
                break
            else:
                print("insert a number")

            
        if user_input == random_number:
            print(f"you get it right at {gussed} guess")
            won = True
            break
        elif abs(user_input - random_number) < 5:
            print("it is burning")
        elif 5 <= abs(user_input - random_number) < 15:
            print("you are close")
        elif 15 <= abs(user_input - random_number) < 25:
            print("try harder")
        else: 
            print("not good")

    if not won:
        print("you lost")
    play_again = input("do you wanna play again? (y/n)").strip().lower()
    if play_again == "n":
        break



    
