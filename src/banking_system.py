# banking_system.py

# Step 1: Initialize account_balance
account_balance = 1000

# Function to display the menu
def display_menu():
    print("\nWelcome to the Basic Banking System")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# Function to handle user input for menu selection
def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect an option (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Function to check balance
def check_balance():
    print(f"Your current balance is: ${account_balance}")

# Function to handle deposit
def deposit(balance, amount=None):
    if amount is None:
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return balance
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:.2f}. Your new balance is ${balance:.2f}.")
    else:
        print("Deposit amount must be positive.")
    return balance

def withdraw(balance, amount=None):
    if amount is None:
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return balance
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${balance:.2f}.")
        else:
            print("Insufficient funds. Please try a smaller amount.")
    else:
        print("Withdrawal amount must be positive.")
    return balance

# Updated  main function to include all functionalities
def main():
    global account_balance
    while True:
        display_menu()  # Display the menu
        user_choice = get_user_choice()  # Get valid user choice

        if user_choice == 1:
            check_balance()  # Show balance
        elif user_choice == 2:
            account_balance = deposit(account_balance)  # Deposit money
        elif user_choice == 3:
            account_balance = withdraw(account_balance)  # Withdraw money
        elif user_choice == 4:
            print("Thank you for banking with us. We cherish you. Goodbye!")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main()
