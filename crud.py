#This is CRUD: Creation, Reading, Updating, and Deletion of database entries

# crud.py
# Firestore CRUD operations for the "users" collection.

def create_user(db, user_data):
    """
    Inserts a new user into Firestore.
    Firestore will auto-generate a document ID unless we specify one.
    We will use user_id as the document ID for easy lookup.
    """
    user_id = str(user_data["user_id"])
    db.collection("users").document(user_id).set(user_data)
    return True


def retrieve_all(db):
    """
    Retrieves all user documents from Firestore.
    Returns a list of dictionaries.
    """
    docs = db.collection("users").stream()
    return [doc.to_dict() for doc in docs]


def get_user_by_id(db, user_id):
    """
    Retrieves a single user by user_id.
    Returns a dictionary or None.
    """
    doc_ref = db.collection("users").document(str(user_id))
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict()
    return None


def update_user(db, user_id, updates):
    """
    Updates a user document with new values.
    """
    doc_ref = db.collection("users").document(str(user_id))
    doc_ref.update(updates)
    return True


def delete_user(db, user_id):
    """
    Deletes a user document from Firestore.
    """
    db.collection("users").document(str(user_id)).delete()
    return True
