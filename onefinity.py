import random


print("Welcome to OneFinity - A number guessing game!")
print("To start playing press enter")
input()

print("Guess a number between 1 and 10")

user_guess = int(input("Enter number: "))
computer_choice = random.randrange(1, 10)

while(user_guess != computer_choice):    
    if(user_guess > computer_choice):
        print("Guessed too high!")
        user_guess = int(input("Guess again: "))
    elif(user_guess < computer_choice):
        print("Guessed too low!")
        user_guess = int(input("Guess again: "))
    else:
        break
    
print("Congratulations, you won.")

