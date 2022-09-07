#number guessing game

import random

computer_guess = random.randint(1,100)

trial = 5
while trial>0:
    user_guess = int(input("enter number : "))
    if user_guess>computer_guess:
        print("HINT : guess lower number ")
    elif user_guess<computer_guess:
        print("HINT: guess higher number ")
    else:
        print("you got it !!")
        trial = 0
    trial-=1
    