import time

time.sleep(30)
user_name_or_email = input("User Name or Email : ")
password = input("Password : ")
doc_ref = db.collection("auth").where("username", "==", user_name_or_email).stream()
usernames = []
for doc_ref_ in doc_ref:
    usernames.append(doc_ref_.to_dict())
doc_ref = db.collection("auth").where("password", "==", password).stream()
passwords = []
for doc_ref_ in doc_ref:
    passwords.append(doc_ref_.to_dict())
emails = []
for doc_ref_ in doc_ref:
    emails.append(doc_ref_.to_dict())
if emails != [] or user_name != [] and password != []:
    print("OK")
