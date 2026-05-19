import random

#Grade Calculator
def grade_calculator():
    base_score = int(input("Enter your base score: "))
    if base_score >= 90:
        print("A")
    elif base_score >= 80:
        print("B")
    elif base_score >= 70:
        print("C")
    elif base_score >= 60:
        print("D")
    else:
        print("F")

#Number Guessing Game
def number_guessing_game():
    secret_number = random.randint(1, 100)
    guesses = 5
    for g in range(guesses):
        guess = int(input("Guess the number between 1 and 100: "))
        
        if guess == secret_number:
            print("Correct! You won!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
            
        print(f"You have {guesses - g - 1} guesses left.\n")
        
    if guess != secret_number:
        print(f"Game Over! The secret number was {secret_number}.")

#Budget Tracker
def budget_tracker():
    # Get the budget from the user
    budget = float(input("What is your budget? R"))
    
    # Get the expense from the user
    expense = float(input("How much did you spend? R"))
    
    # Calculate remaining
    remaining = budget - expense
    
    # Tell them how much is left
    print(f"You have R{remaining} left to spend.")

      
        
        