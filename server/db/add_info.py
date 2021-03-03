import firebase_admin
from firebase_admin import credentials, firestore

config = {
    "type": "",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": "",
}
cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
db = firestore.client()


def add_info(info):
    doc_ref = db.collection("info").document()
    doc_ref.set(info)