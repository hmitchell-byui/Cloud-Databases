# questions.py
# Handles all user input for creating new user records.
# This module contains no database logic—only input collection and structuring.


def ask_basic_info():
    """
    Collects basic user information through input prompts.

    Returns:
        A dictionary containing:
            f_name, l_name, email, phone, sex, title, height, weight

    Notes:
        - Height and weight are validated as floats.
        - All other fields are stored as strings.
    """
    print("\n--- New User Setup ---")

    f_name = input("First name: ").strip()
    l_name = input("Last name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone number: ").strip()
    sex = input("Sex (M/F): ").strip()
    title = input("Title (Mr, Ms, Dr, etc.): ").strip()

    # Height validation
    while True:
        try:
            height = float(input("Height (in inches): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Weight validation
    while True:
        try:
            weight = float(input("Weight (in pounds): "))
            break
        except ValueError:
            print("Please enter a valid number.")

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
    """
    Prompts the user to select a clearance level.

    Returns:
        A string: "admin", "user", or "guest".

    Behavior:
        - Loops until a valid selection is made.
    """
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
    Generates a user_id based on clearance level and existing user count.

    Args:
        clearance: "admin", "user", or "guest".
        existing_users_count: Number of users currently in Firestore.

    Returns:
        An integer user_id.

    Rules:
        - Admin IDs start at 1000
        - User IDs start at 2000
        - Guest IDs start at 3000
        - Each new user increments the offset
    """
    if clearance == "admin":
        return 1000 + existing_users_count
    elif clearance == "user":
        return 2000 + existing_users_count
    elif clearance == "guest":
        return 3000 + existing_users_count


def collect_new_user(existing_users_count):
    """
    Full pipeline for creating a new user record.

    Steps:
        1. Collect basic info
        2. Ask for clearance level
        3. Generate user_id
        4. Combine all fields into a single dictionary

    Args:
        existing_users_count: Number of users currently in Firestore.

    Returns:
        A complete user_data dictionary ready for Firestore insertion.
    """
    user_data = ask_basic_info()
    clearance = assign_clearance()
    user_id = generate_user_id(clearance, existing_users_count)

    user_data["clearance"] = clearance
    user_data["user_id"] = user_id

    return user_data
