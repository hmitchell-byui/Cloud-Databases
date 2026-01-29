# This is to help pull and push the latest changes to the repository

# save.py
# Handles staging of changes and user confirmation before committing to CRUD operations.

import ui


def confirm_changes(data_dict):
    """
    Shows the user the pending changes and asks for confirmation.
    Returns True if the user confirms, False otherwise.
    """

    ui.print_header("Review Pending Changes")

    for key, value in data_dict.items():
        print(f"{key}: {value}")

    print("\nDo you want to commit these changes?")
    choice = input("Confirm (y/n): ").strip().lower()

    return choice == "y"


def confirm_delete(identifier):
    """
    Asks the user to confirm deletion of a record.
    Returns True if confirmed, False otherwise.
    """

    ui.print_header("Confirm Delete")

    print(f"You are about to delete user with ID: {identifier}")
    choice = input("Are you absolutely sure? (y/n): ").strip().lower()

    return choice == "y"


def stage_update(existing_data, updates):
    """
    Creates a staged version of updated data.
    - existing_data: dict of current values
    - updates: dict of new values
    Returns a merged dictionary representing the staged update.
    """

    staged = existing_data.copy()

    for key, value in updates.items():
        staged[key] = value

    return staged
