# save.py
# Handles staging and confirmation of changes before committing them to Firestore.
# This module contains no database logic and no UI decisions beyond simple prompts.

import ui


def confirm_changes(data_dict):
    """
    Displays pending changes and asks the user to confirm.

    Args:
        data_dict: Dictionary of fields that will be written to Firestore.

    Returns:
        True if the user confirms, False otherwise.

    Behavior:
        - Prints each key/value pair for review.
        - Prevents accidental writes by requiring explicit confirmation.
    """
    ui.print_header("Review Pending Changes")

    for key, value in data_dict.items():
        print(f"{key}: {value}")

    print("\nDo you want to commit these changes?")
    choice = input("Confirm (y/n): ").strip().lower()

    return choice == "y"


def confirm_delete(identifier):
    """
    Asks the user to confirm deletion of a user record.

    Args:
        identifier: The user_id of the record to delete.

    Returns:
        True if the user confirms deletion, False otherwise.

    Behavior:
        - Displays a warning message.
        - Requires explicit confirmation to avoid accidental data loss.
    """
    ui.print_header("Confirm Delete")

    print(f"You are about to delete user with ID: {identifier}")
    choice = input("Are you absolutely sure? (y/n): ").strip().lower()

    return choice == "y"


def stage_update(existing_data, updates):
    """
    Creates a merged dictionary representing the final state after updates.

    Args:
        existing_data: Dictionary of the current stored user data.
        updates: Dictionary of fields the user wants to change.

    Returns:
        A new dictionary containing:
            - All original fields
            - Updated fields overwritten by values in 'updates'

    Purpose:
        - Allows the user to preview the final result before committing.
    """
    staged = existing_data.copy()

    for key, value in updates.items():
        staged[key] = value

    return staged
