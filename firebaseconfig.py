import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account key
cred = credentials.Certificate("C:/Users/Admin/OneDrive/Desktop/Face Recognition System/face-recognition-7c83d-firebase-adminsdk-h6dpo-755a1cdd56.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
