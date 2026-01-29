# Hopefully the user interface code will go here

# ui.py
# Handles all user-facing display and menu logic.
# No database logic. No business logic. Just presentation.

def print_header(title):
    """Prints a formatted section header."""
    print("\n" + "=" * 40)
    print(f"{title}")
    print("=" * 40)


def success(message):
    """Displays a success message."""
    print(f"\n✔ SUCCESS: {message}")


def warning(message):
    """Displays a warning or error message."""
    print(f"\n⚠ WARNING: {message}")


def goodbye():
    """Displays a closing message."""
    print("\nExiting program. Goodbye!")


# -----------------------------
# CRUD MENU
# -----------------------------
def crud_menu():
    """Displays the CRUD menu and returns the user's choice."""
    print("\nChoose an operation:")
    print("1. Retrieve all users")
    print("2. Update a user")
    print("3. Delete a user")
    print("4. Exit")

    return input("Enter choice (1-4): ").strip()


# -----------------------------
# USER INPUT HELPERS
# -----------------------------
def ask_for_user_id():
    """Prompts the user for a user_id."""
    return input("\nEnter user ID: ").strip()


def ask_for_update_fields():
    """
    Prompts the user for fields to update.
    Returns a dictionary of updates.
    """
    print("\nEnter new values (leave blank to skip):")

    updates = {}
    fields = ["f_name", "l_name", "email", "phone", "sex", "title", "height", "weight"]

    for field in fields:
        value = input(f"{field}: ").strip()
        if value != "":
            updates[field] = value

    return updates


# -----------------------------
# DISPLAY HELPERS
# -----------------------------
def display_data(data_list):
    """
    Displays a list of user dictionaries.
    Expects: [ {user}, {user}, ... ]
    """
    print_header("User Records")

    if not data_list:
        print("No records found.")
        return

    for record in data_list:
        print("-" * 40)
        for key, value in record.items():
            print(f"{key}: {value}")
    print("-" * 40)
