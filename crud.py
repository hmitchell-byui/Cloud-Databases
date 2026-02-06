# crud.py
# Handles all Firestore CRUD operations for the "users" collection.
# This module contains no UI logic and no input prompts—only database actions.


def create_user(db, user_data):
    """
    Creates a new user document in Firestore.

    Args:
        db: Firestore client instance.
        user_data: Dictionary containing all user fields.

    Behavior:
        - Uses user_id as the Firestore document ID for predictable lookups.
        - Overwrites any existing document with the same ID.
    """
    user_id = str(user_data["user_id"])
    db.collection("users").document(user_id).set(user_data)
    return True


def retrieve_all(db):
    """
    Retrieves all user documents from Firestore.

    Args:
        db: Firestore client instance.

    Returns:
        A list of dictionaries, one per user document.
    """
    docs = db.collection("users").stream()
    return [doc.to_dict() for doc in docs]


def get_user_by_id(db, user_id):
    """
    Retrieves a single user document by user_id.

    Args:
        db: Firestore client instance.
        user_id: The ID of the user to retrieve.

    Returns:
        A dictionary of user data if found, otherwise None.
    """
    doc_ref = db.collection("users").document(str(user_id))
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict()
    return None


def update_user(db, user_id, updates):
    """
    Updates an existing user document.

    Args:
        db: Firestore client instance.
        user_id: The ID of the user to update.
        updates: Dictionary of fields to update.

    Behavior:
        - Only updates the fields provided in 'updates'.
        - Does not overwrite the entire document.
    """
    doc_ref = db.collection("users").document(str(user_id))
    doc_ref.update(updates)
    return True


def delete_user(db, user_id):
    """
    Deletes a user document from Firestore.

    Args:
        db: Firestore client instance.
        user_id: The ID of the user to delete.

    Behavior:
        - Removes the document entirely.
    """
    db.collection("users").document(str(user_id)).delete()
    return True
