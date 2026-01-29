import firebase_admin
from firebase_admin import credentials, firestore

def initialize_system():
    cred = credentials.Certificate("serviceAccount.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
