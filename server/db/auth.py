import firebase_admin
from firebase_admin import credentials, firestore
import requests
from server.db.send_email import *

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
# firebase_admin.initialize_app(cred)
db = firestore.client()


class Sign_Up:
    def __init__(self, email, password, user_name):
        self.email = email
        self.password = password
        self.user_name = user_name
        self.info = {
            "email": self.email,
            "username": self.user_name,
            "password": self.password,
        }

    def check_user_name_and_password(self):
        try:
            doc_ref = (
                db.collection("auth").where("password", "==", self.password).stream()
            )
            passwords = []
            for doc_ref_ in doc_ref:
                passwords.append(doc_ref_.to_dict())
            doc_ref = (
                db.collection("auth").where("username", "==", self.user_name).stream()
            )
            user_names = []
            for doc_ref_ in doc_ref:
                user_names.append(doc_ref_.to_dict())
            print(passwords)
            print(user_names)
            if self.info not in passwords and self.info not in user_names:
                return True
            return False
        except:
            return False

    def check_email_and_password(self):
        try:
            doc_ref = (
                db.collection("auth").where("password", "==", self.password).stream()
            )
            passwords = []
            for doc_ref_ in doc_ref:
                passwords.append(doc_ref_.to_dict())
            doc_ref = db.collection("auth").where("email", "==", self.email).stream()
            emails = []
            for doc_ref_ in doc_ref:
                emails.append(doc_ref_.to_dict())
            print(passwords)
            print(emails)
            if self.info not in passwords and self.info not in emails:
                return True
            return False
        except:
            return False

    def check_email_validitiy(self) -> bool:
        url = "https://isitarealemail.com/api/email/validate"
        request_result = requests.get(
            url,
            {"email": self.email},
        )
        result = request_result.json()["status"]
        if result == "valid":
            return True
        return False

    def add_to_db(self):
        try:
            su = Sign_Up(
                email=self.email, password=self.password, user_name=self.password
            )
            results = [
                su.check_email_and_password(),
                su.check_user_name_and_password(),
                su.check_email_validitiy(),
            ]
            if False not in results:
                doc_ref = db.collection("auth").document()
                doc_ref.set(self.info)
                send_mail(
                    to_email=self.email,
                    subject="New Account Created ! ",
                    body="New Account Created ! ",
                )
                return [True, ["New Account Created ! "]]
            errors = []
            if results[0] is False:
                errors.append("There is someone using the same email and password")
            if results[1] is False:
                errors.append("There is someone using the same user name and password")
            if results[2] is False:
                errors.append("Your Email is not valied ! ")
            return [False, errors]
        except:
            return [False, ["An Error Occured ! "]]



class Sign_In:
    def __init__(self, user_name_or_email, password):
        self.user_name_or_email = user_name_or_email
        self.password = password

    def check_user_name_and_password(self):
        doc_ref = db.collection("auth").where("password", "==", self.password).stream()
        passwords = []
        for doc_ref_ in doc_ref:
            passwords.append(doc_ref_.to_dict())
        doc_ref = db.collection("auth").where("username", "==", self.user_name_or_email).stream()
        user_names = []
        for doc_ref_ in doc_ref:
            user_names.append(doc_ref_.to_dict())
        print(user_names)
        print(passwords)
        if passwords != [] and user_names != []:
            return True
        return False

    def check_email_and_password(self):
        doc_ref = db.collection("auth").where("password", "==", self.password).stream()
        passwords = []
        for doc_ref_ in doc_ref:
            passwords.append(doc_ref_.to_dict())
        doc_ref = (
            db.collection("auth").where("email", "==", self.user_name_or_email).stream()
        )
        emails = []
        for doc_ref_ in doc_ref:
            emails.append(doc_ref_.to_dict())
        print(emails)
        print(passwords)
        if passwords != [] and emails != []:
            return True
        return False

    def check(self):
        si = Sign_In(
            user_name_or_email=self.user_name_or_email, password=self.password
        )
        results = [si.check_email_and_password(), si.check_user_name_and_password()]
        if results[0] is True or results[1] is True:
            send_mail(
                to_email=self.user_name_or_email,
                subject="Loged In",
                body="Loged In",
            )
            return [True, ["loged in successfully ! "]]
        return [False, ["Please Check you user name or email and your password ! "]]

