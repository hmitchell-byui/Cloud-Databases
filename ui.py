# ui.py
# Handles all user-facing display, formatting, and menu interactions.
# Contains no business logic and no database operations.


def print_header(title):
    """
    Prints a formatted section header for readability.

    Args:
        title: The title text to display.
    """
    print("\n" + "=" * 40)
    print(f"{title}")
    print("=" * 40)


def success(message):
    """
    Displays a success message.

    Args:
        message: Text describing the successful action.
    """
    print(f"\n✔ SUCCESS: {message}")


def warning(message):
    """
    Displays a warning or error message.

    Args:
        message: Text describing the issue.
    """
    print(f"\n⚠ WARNING: {message}")


def goodbye():
    """
    Displays a closing message when the program exits.
    """
    print("\nExiting program. Goodbye!")


def crud_menu():
    """
    Displays the CRUD menu and returns the user's choice.

    Returns:
        A string representing the user's menu selection.
    """
    print("\nChoose an operation:")
    print("1. Retrieve all users")
    print("2. Update a user")
    print("3. Delete a user")
    print("4. Exit")

    return input("Enter choice (1-4): ").strip()


def ask_for_user_id():
    """
    Prompts the user to enter a user_id.

    Returns:
        The user_id as a string.
    """
    return input("\nEnter user ID: ").strip()


def ask_for_update_fields():
    """
    Prompts the user for fields to update.

    Returns:
        A dictionary of updates where:
            - Keys are field names
            - Values are new values entered by the user

    Behavior:
        - Blank input means "skip this field"
        - Height and weight should be numeric, but validation is handled elsewhere
    """
    print("\nEnter new values (leave blank to skip):")

    updates = {}
    fields = ["f_name", "l_name", "email", "phone", "sex", "title", "height", "weight"]

    for field in fields:
        value = input(f"{field}: ").strip()
        if value != "":
            updates[field] = value

    return updates


def display_data(data_list):
    """
    Displays a list of user dictionaries in a readable format.

    Args:
        data_list: List of dictionaries representing user records.

    Behavior:
        - Prints each record with separators
        - Handles empty lists gracefully
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
