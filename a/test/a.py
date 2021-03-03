import firebase_admin
from firebase_admin import credentials, firestore
import requests

config = {
    "type": "service_account",
    "project_id": "auth-app-firebase-firesore-rd",
    "private_key_id": "95c39265a8a723459fef05765c6a358a09fb6427",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDI/d9Hj0Ci/Pne\nnS21O4+RYJG8VAFsfSpn0IZeSDHdnFurqk84CsXKHV8dXpDsNWkHFzCWYH51LvzE\n32WIP/UCHsVkK1dNW6vYMN6HR/5HIjQbDaCioUBCOFWzt0RRUtu6imG4wlSNYLP+\nI/HgWzaHTSmVz9lahAH1bXrG/9bXVhHzk33i2qr45vzENNDLYRy0ACQnpZzZH+1D\ndxAnClglrLb1ITQM1kSpKabvgfXKCES/mWkUb+jrvycYkWcDUnPlvhtpbKaUKsT7\nK2V5U0qXaDTHdfcxrLcY74UZ6rHEiT64loqLdq18n5ZlnE5OUttFkkL37jcvbAP9\nZ5O6UzzhAgMBAAECggEALqjjIgNzU7MrVb8C+rEMTAlRY9lTqEopY0bhPrd/Xg1b\nqa9Eq0Oy9ZAageCvf6qJipQbWzmk+dLR6ulasoX4fMjEddPq9UI8E1kK+/heY0ih\nNIuWGFMbbhQSb0FzKnb0HCrec0wn4VdLCctx7i32q3PiHM2PDaiaJM4I4/RGPaBr\n+pcFuFUVg26ubxJyzgCsYRi8R8XCovaXeg9DG5bXmOVythhG+sQeOgKY4dLx9Nuh\nDiwXBSRCpyb4A5jFAArvMSAnyM440VQUZKiBta9kW3EOVJixS70cF9Mj3q01W+Al\nZEedalJgHHesC8iLm7JsIGkcAQMwGbxI2sJPJo2nrQKBgQDoQJESZDiP0unTzU7T\njoBPcS5XQRh0KqHTWEXHRSi3uhJR+KzaHAGdJtXbp0e7yrLITt/o+3rb5eaHBXJm\nUNacaUORdrq8ue+/XBh7lHcIQigaFAuek84mzRelWyx5gxfYkolLn4b7jIjgHoJR\n2N4G0rTgK6LHnDPE9KeGffOMnQKBgQDdiweyuifMTMhuyQX8jqIoy8EmCspZcdv4\n3ofodRVI1/sRf1RzmaS2R8uyNC11hQfCIUKDkos1UshUlQ7DgMRrDVoLZdmeCmOl\nOTnNMHJezCwFjlWBHVa+jY34MDw+gVUcBYBHqOZHFKbaxDIA3Pz+54JlEDX/SBm5\n2Dl56ktEFQKBgQCQxOZo02XaaLruFjTDdDkQy9j59I6copJandRpAPf/hhGzXNHJ\n5tkury1xDJWPPisw5tF1dYRAm86VbVTA6DTOLGM8wghmaXRDENIF/iYwVKSQlNwl\nTbabww2xOeLAH3H2wmioZdkK5a/QG9RZ1leXYzHx5eFCkWBHrcTa9ZmhlQKBgAbI\n1jCEAOoBw/WYlGVanN6w9rZKiE3a7cieT/0vcLptWtP7WUO9Bc1LP5KyhF3f+A/a\n4uWSnE7CvT3R3sTf8aPxobtNoC910/1gVkPRYv9CM2rsI/QzSM/HF/zsxTuIzGly\nRa5sHrk4ia+TaJCcM+c+gcDEkVLDC36kf4YbRbjNAoGAYqThq+gQ3Cx6lgPzXI4j\nLUGWL+oV6c798YHWyA3oxQbzCrxOkBoXNpsaRYEWID68sx8Ft0QoQsSmMVuUydfi\nwrQ69v827IizlW6OyoIfpWLpV1VXJ7pxDAMUNPO3r0BI90oVk1LRVYU9RuYKPnh5\nyRjCz3TjxnkzGOEKxLUsLlM=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-jw5t0@auth-app-firebase-firesore-rd.iam.gserviceaccount.com",
    "client_id": "100506291617455837166",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jw5t0%40auth-app-firebase-firesore-rd.iam.gserviceaccount.com",
}
cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
db = firestore.client()


class Sign_In:
    def __init__(self, user_name_or_email, password):
        self.user_name_or_email = user_name_or_email
        self.password = password

    def check_user_name_and_password(self):
        doc_ref = db.collection("auth").where("password", "==", self.password).stream()
        passwords = []
        for doc_ref_ in doc_ref:
            passwords.append(doc_ref_.to_dict())
        doc_ref = (
            db.collection("auth")
            .where("username", "==", self.user_name_or_email)
            .stream()
        )
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
        si = Sign_In(user_name_or_email=self.user_name_or_email, password=self.password)
        results = [si.check_email_and_password(), si.check_user_name_and_password()]
        if results[0] is True or results[1] is True:
            # send_mail(
            #     to_email=self.user_name_or_email,
            #     subject="Loged In",
            #     body="Loged In",
            # )
            return [True, ["loged in successfully ! "]]
        return [False, ["Please Check you user name or email and your password ! "]]


si = Sign_In(user_name_or_email="go2ranuga@gmail.com", password="LOL")
result = si.check()
print(result)
