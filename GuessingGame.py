import random

number=random.randint(1, 9)
chances=0

print("Guess a number between 1 and 9")

while(chances<5):
    guess=int(input("Enter your guess: "))
    if(guess==number):
        print("Congratulations you win")
        break
    elif(guess<number):
        print("Your guess is too low. Guess a highe number")
    else:
        print("Your guess is too high. Guess a lower number")
    chances=chances+1

if not chances<5:
    print("You Lose. The number is ",number)