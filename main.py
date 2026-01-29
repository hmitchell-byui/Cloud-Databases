# Main logic

# main.py
# Orchestrates the full program flow:
# - Initialization
# - User decision tree
# - New user onboarding
# - CRUD menu loop

import ui
import questions
import save
import crud


def initialize_system():
    """
    Placeholder for Firebase initialization.
    Later this will load credentials and create the Firestore client.
    """
    print("Initializing system...")
    db = None  # Placeholder until Firestore is added
    return db


def check_if_user_exists():
    """
    Placeholder logic.
    Later this will query Firestore for a user.
    For now, ask the user manually.
    """
    ui.print_header("User Login")

    choice = input("Are you a returning user? (y/n): ").strip().lower()
    return choice == "y"


def onboarding_flow(existing_users_count):
    """
    Handles new user creation:
    - Ask questions
    - Stage data
    - Confirm
    - Commit
    """
    ui.print_header("New User Setup")

    # Collect user data
    user_data = questions.collect_new_user(existing_users_count)

    # Stage + confirm
    confirmed = save.confirm_changes(user_data)

    if confirmed:
        crud.create_user(user_data)
        ui.success("User created successfully.")
        return user_data
    else:
        ui.warning("User creation canceled.")
        return None


def crud_menu_loop():
    """
    Main CRUD loop for returning users.
    """
    while True:
        ui.print_header("CRUD Operations")

        choice = ui.crud_menu()

        if choice == "1":
            data = crud.retrieve_all()
            ui.display_data(data)

        elif choice == "2":
            user_id = ui.ask_for_user_id()
            updates = ui.ask_for_update_fields()
            staged = save.confirm_changes(updates)
            if staged:
                crud.update_user(user_id, updates)
                ui.success("User updated.")
            else:
                ui.warning("Update canceled.")

        elif choice == "3":
            user_id = ui.ask_for_user_id()
            staged = save.confirm_delete(user_id)
            if staged:
                crud.delete_user(user_id)
                ui.success("User deleted.")
            else:
                ui.warning("Delete canceled.")

        elif choice == "4":
            ui.goodbye()
            break

        else:
            ui.warning("Invalid choice. Try again.")


def main():
    """
    Full program execution.
    """
    db = initialize_system()

    # Placeholder: count existing users
    existing_users_count = 0

    user_exists = check_if_user_exists()

    if not user_exists:
        new_user = onboarding_flow(existing_users_count)
        if new_user:
            existing_users_count += 1
            ui.success("Redirecting to main menu...")

    crud_menu_loop()


if __name__ == "__main__":
    main()
