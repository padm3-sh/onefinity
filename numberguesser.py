import random


print("Welcome to this Number Guesser Game!")
print("To start playing press enter")
input()

print("Guess a number between 1 and 10")

user_guess = int(input("Enter number: "))
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer_choice = random.choice(list_of_numbers)

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

