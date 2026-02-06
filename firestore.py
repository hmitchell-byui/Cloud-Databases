# firestore.py
# Handles Firestore initialization and returns a database client.
# This module contains no CRUD logic—only setup.


import firebase_admin
from firebase_admin import credentials, firestore


def initialize_firestore():
    """
    Initializes the Firebase Admin SDK and returns a Firestore client.

    Behavior:
        - Loads serviceAccount.json credentials
        - Initializes the Firebase app (only once per runtime)
        - Returns a Firestore client instance for database operations

    Returns:
        Firestore client object
    """
    cred = credentials.Certificate("serviceAccount.json")

    # Initialize only once; firebase_admin prevents duplicate initialization
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
