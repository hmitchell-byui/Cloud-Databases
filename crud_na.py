# crud.py
# Placeholder CRUD operations.
# Later, these functions will connect to Firestore.
# For now, they operate on a simple in-memory list for testing.

# Temporary in-memory "database"
mock_db = []


def create_user(user_data):
    """
    Inserts a new user into the mock database.
    Later this will insert into Firestore.
    """
    mock_db.append(user_data)
    return True


def retrieve_all():
    """
    Returns all user records.
    Later this will query Firestore.
    """
    return mock_db


def get_user_by_id(user_id):
    """
    Retrieves a single user by user_id.
    """
    for user in mock_db:
        if str(user.get("user_id")) == str(user_id):
            return user
    return None


def update_user(user_id, updates):
    """
    Updates a user record with new values.
    Later this will update Firestore.
    """
    for user in mock_db:
        if str(user.get("user_id")) == str(user_id):
            for key, value in updates.items():
                user[key] = value
            return True
    return False


def delete_user(user_id):
    """
    Deletes a user record.
    Later this will delete from Firestore.
    """
    global mock_db
    mock_db = [user for user in mock_db if str(user.get("user_id")) != str(user_id)]
    return True
