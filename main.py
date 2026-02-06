# main.py
# Orchestrates the entire program:
# - Firestore initialization
# - Login or onboarding
# - CRUD menu loop
# This file acts as the high‑level controller for all modules.

import ui
import questions
import save
import crud
import firestore


def initialize_system():
    """
    Initializes the Firestore database connection.
    Delegates to firestore.initialize_firestore() which loads the
    service account credentials and returns a Firestore client.
    """
    ui.print_header("Initializing Cloud Database")
    db = firestore.initialize_firestore()
    return db


def login_flow(db):
    """
    Handles returning‑user authentication using:
    - user_id lookup
    - email OR phone validation

    Returns:
        user dict if login succeeds
        None if login fails
    """
    ui.print_header("User Login")

    # Step 1: Ask for user_id
    user_id = input("Enter your user ID: ").strip()
    user = crud.get_user_by_id(db, user_id)

    if not user:
        ui.warning("No user found with that ID.")
        return None

    # Step 2: Choose validation method
    print("\nValidation required.")
    print("1. Validate with email")
    print("2. Validate with phone")

    choice = input("Choose method (1/2): ").strip()

    # Step 3: Validate email
    if choice == "1":
        email = input("Enter your email: ").strip()
        if email == user["email"]:
            ui.success("Login successful.")
            return user
        else:
            ui.warning("Email does not match.")
            return None

    # Step 4: Validate phone
    elif choice == "2":
        phone = input("Enter your phone number: ").strip()
        if phone == user["phone"]:
            ui.success("Login successful.")
            return user
        else:
            ui.warning("Phone number does not match.")
            return None

    # Invalid choice
    else:
        ui.warning("Invalid choice.")
        return None


def onboarding_flow(db, existing_users_count):
    """
    Handles new‑user creation:
    - Collects questionnaire data
    - Assigns clearance + user_id
    - Shows staged data for confirmation
    - Commits to Firestore if approved

    Returns:
        user_data dict if creation succeeds
        None if canceled
    """
    ui.print_header("New User Setup")

    # Ask questions and build user dictionary
    user_data = questions.collect_new_user(existing_users_count)

    # Show staged data and ask for confirmation
    confirmed = save.confirm_changes(user_data)

    if confirmed:
        crud.create_user(db, user_data)
        ui.success("User created successfully.")
        return user_data
    else:
        ui.warning("User creation canceled.")
        return None


def crud_menu_loop(db):
    """
    Main CRUD loop for authenticated users.
    Provides options to:
    - Retrieve all users
    - Update a user
    - Delete a user
    - Exit program

    Runs until the user chooses to exit.
    """
    while True:
        ui.print_header("CRUD Operations")
        choice = ui.crud_menu()

        # Retrieve all users
        if choice == "1":
            data = crud.retrieve_all(db)
            ui.display_data(data)

        # Update a user
        elif choice == "2":
            user_id = ui.ask_for_user_id()
            existing = crud.get_user_by_id(db, user_id)

            if not existing:
                ui.warning("User not found.")
                continue

            updates = ui.ask_for_update_fields()

            # Merge existing + updates for preview
            staged = save.stage_update(existing, updates)

            if save.confirm_changes(staged):
                crud.update_user(db, user_id, updates)
                ui.success("User updated.")
            else:
                ui.warning("Update canceled.")

        # Delete a user
        elif choice == "3":
            user_id = ui.ask_for_user_id()
            existing = crud.get_user_by_id(db, user_id)

            if not existing:
                ui.warning("User not found.")
                continue

            if save.confirm_delete(user_id):
                crud.delete_user(db, user_id)
                ui.success("User deleted.")
            else:
                ui.warning("Delete canceled.")

        # Exit
        elif choice == "4":
            ui.goodbye()
            break

        # Invalid input
        else:
            ui.warning("Invalid choice. Try again.")


def main():
    """
    Entry point for the entire application.
    Steps:
    1. Initialize Firestore
    2. Count existing users
    3. Ask if returning or new user
    4. Run login or onboarding
    5. Enter CRUD loop
    """
    db = initialize_system()

    # Count existing users to generate correct user_id ranges
    existing_users_count = len(crud.retrieve_all(db))

    returning = input("Are you a returning user? (y/n): ").strip().lower()

    # Returning user → login
    if returning == "y":
        logged_in = login_flow(db)
        if not logged_in:
            ui.warning("Login failed. Exiting.")
            return

    # New user → onboarding
    else:
        new_user = onboarding_flow(db, existing_users_count)
        if new_user:
            existing_users_count += 1
            ui.success("Redirecting to main menu...")
        else:
            ui.warning("Setup failed. Exiting.")
            return

    # Enter CRUD menu
    crud_menu_loop(db)


if __name__ == "__main__":
    main()
