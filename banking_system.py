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

# Main function to start the program
def main():
    print(f"Initial account balance: ${account_balance}")
    while True:
        display_menu()  # Display the menu
        user_choice = get_user_choice()  # Get valid user choice
        print(f"You selected option {user_choice}")
        # Further actions will be added in subsequent steps

if __name__ == "__main__":
    main()
1