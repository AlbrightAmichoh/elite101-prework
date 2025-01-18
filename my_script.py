def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def ask_how_old_():
    return input("What is your age? ")

def display_menu():
    menu_items = [
        "1. Coffee - $3.99",
        "2. Tea - $5.38",
        "3. Soda - $2.99",
        "4. Chips - $3.58",
        "5. Exit"
    ]
    
    print("\nHere is our menu:")
    for item in menu_items:
        print(item)
    
    # Ask for user selection
    try:
        choice = int(input("\nPlease select an item by number (1-5): "))
        if 1 <= choice <= 4:
            print(f"You bought: {menu_items[choice - 1]}")
        elif choice == 5:
            print("Thank you for shopping with us! Goodbye!")
            return False  
        else:
            print("Invalid choice, please select a number between 1 and 5.")
            return True 
    except ValueError:
        print("Invalid input, please enter a number.")
        return True  

def main():
    print("Welcome to our store! How may I help you today?")
    user_name = get_user_name()
    greet_user(user_name)
    user_age = ask_how_old_()
    print(f"It's nice to be {user_age} years old. Let me show you our menu.")
    
    
    while True:
        if not display_menu():
            break  

if __name__ == "__main__":
    main()
