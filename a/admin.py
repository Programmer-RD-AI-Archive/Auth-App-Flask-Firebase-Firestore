import firebase_admin
from firebase_admin import credentials, firestore

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
doc_ref = db.collection("auth").stream()
for doc in doc_ref:
    print("\n User Auth Info \n")
    print(doc.to_dict())
    print("\n User Auth Info \n")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("*"*50)
print("*"*50)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
doc_ref_ = db.collection("info").stream()
for doc in doc_ref_:
    print("\n User Info \n")
    print(doc.to_dict())
    print("\n User Info \n")
