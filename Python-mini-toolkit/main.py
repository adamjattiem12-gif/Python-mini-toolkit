from helpers import grade_calculator, number_guessing_game, budget_tracker

#Python Mini Toolkit Menu
def show_menu():
    print("Welcome to Adam's Python Mini Toolkit!")
    print("Please select an option:")
    print("1. Grade Calculator")
    print("2. Number Guessing Game")
    print("3. Budget Tracker")
    print("4. Exit")
    choice = input("Please enter your choice (1-4): ")
    return choice

#Menu Selector
def main():
    choice = show_menu()
    if choice == "1":
        grade_calculator()
    elif choice ==  "2":
        number_guessing_game()
    elif choice == "3":
        budget_tracker()
    elif choice == "4":
        print("Thanks for using Adam's Python Mini Toolkit!")
    else:
        print("Invalid choice.")
main()
    
