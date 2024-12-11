import firebase_admin
from firebase_admin import credentials, firestore
import os

def initialize_firebase():
    """Initialize Firebase Admin SDK"""
    try:
        if not firebase_admin._apps:  # Check if already initialized
            private_key = os.environ.get("FIREBASE_PRIVATE_KEY", "")
            if private_key:
                # Handle both escaped and unescaped newlines
                private_key = private_key.replace('\\n', '\n')
                if not private_key.startswith('-----BEGIN PRIVATE KEY-----'):
                    print("Warning: Private key does not have the expected format")
                print("Private key length:", len(private_key))
                print("Private key first 50 chars:", private_key[:50])
                
            cred_dict = {
                "type": "service_account",
                "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
                "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
                "private_key": private_key,
                "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
                "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL")
            }
            
            # Print debug information
            print("Credential Dictionary:")
            for key, value in cred_dict.items():
                if key != "private_key":
                    print(f"{key}: {value}")
                else:
                    print(f"{key}: [REDACTED]")
            
            cred = credentials.Certificate(cred_dict)
            
            print("Initializing Firebase with project ID:", os.environ.get("FIREBASE_PROJECT_ID"))
            firebase_admin.initialize_app(cred)
            
        return firestore.client()
    except Exception as e:
        print(f"Error initializing Firebase: {str(e)}")
        print("Project ID:", os.environ.get("FIREBASE_PROJECT_ID"))
        print("Client Email:", os.environ.get("FIREBASE_CLIENT_EMAIL"))
        return None

def save_form_data(collection_name, data):
    """Save form data to Firestore"""
    try:
        db = firestore.client()
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(data)
        return True, doc_ref.id
    except Exception as e:
        print(f"Error saving to Firestore: {e}")
        return False, str(e)
