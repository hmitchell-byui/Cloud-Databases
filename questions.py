# This is for the questionaire that fuels the database

# questions.py
# Handles all user input and returns a structured dictionary of user data.

def ask_basic_info():
    """Collects basic user information from prompts."""
    print("\n--- New User Setup ---")

    f_name = input("First name: ").strip()
    l_name = input("Last name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone number: ").strip()
    sex = input("Sex (M/F): ").strip()
    title = input("Title (Mr, Ms, Dr, etc.): ").strip()

    # Height and weight with basic validation
    while True:
        try:
            height = float(input("Height (in inches): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            weight = float(input("Weight (in pounds): "))
            break
        except ValueError:
            print("Please enter a valid number.")

# Return collected data as a dictionary
    return {
        "f_name": f_name,
        "l_name": l_name,
        "email": email,
        "phone": phone,
        "sex": sex,
        "title": title,
        "height": height,
        "weight": weight
    }


def assign_clearance():
    """Asks the user for a clearance level and returns it."""
    print("\nClearance Levels:")
    print("1. Admin")
    print("2. User")
    print("3. Guest")

    while True:
        choice = input("Select clearance level (1-3): ").strip()

        if choice == "1":
            return "admin"
        elif choice == "2":
            return "user"
        elif choice == "3":
            return "guest"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def generate_user_id(clearance, existing_users_count):
    """
    Auto-assigns a user_id based on clearance level and existing user count.
    - System administrator is always user_id = 0
    - Admins start at 1000
    - Users start at 2000
    - Guests start at 3000
    """
    if clearance == "admin":
        return 1000 + existing_users_count
    elif clearance == "user":
        return 2000 + existing_users_count
    elif clearance == "guest":
        return 3000 + existing_users_count


def collect_new_user(existing_users_count):
    """
    Full pipeline for creating a new user:
    - Ask basic info
    - Ask clearance
    - Assign user_id
    - Return full user dictionary
    """
    user_data = ask_basic_info()
    clearance = assign_clearance()
    user_id = generate_user_id(clearance, existing_users_count)

    user_data["clearance"] = clearance
    user_data["user_id"] = user_id

    return user_data
