import random
import os


def main():
    print("Welcome to OneFinity - A number guessing game!")
    print("1. Number Guesser")
    print("2. Word Guesser")
    choice = int(input("Enter choice: "))

    if choice == 1:
        os.system('clear')
        number_guesser()
    elif choice == 2:
        os.system('clear')
        word_guesser()
    else:
        print("Incorrect option entered!")
        exit

def number_guesser():
    print("The computer will choose a number between 1 - 10")
    print("You have to guess it")

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
    
  
def word_guesser():
    print("The computer will choose a number and give you hints.")
    print("You have to guess it.")
    
    random_words = ["hello", "world", "panther", "columbia", "zero"]
    chosen_word = random.choice(random_words)
    
    print(f"The word starts with {chosen_word[0]} and ends with {chosen_word[-1]}. The word also has {len(chosen_word)} letters.")
    guessed_word = input("Enter guess: ")
    
    if guessed_word == chosen_word:
        print("Right, you won!")
    else:
        print("That is not right.")
    