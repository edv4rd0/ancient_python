from pymongo import MongoClient
import hashlib

SALT = 'c7425a7bec3f446493a08bf6f1bed422'

# This is a simple script to run to set up the database


client = MongoClient('localhost', 27017)

db = client.python_challenge


password = hashlib.sha512('password' + SALT).hexdigest()

user = {"username": "user", 
        "password": password, 
        "add_record": True, 
        "edit_record": True, 
        "remove_record": True, 
        "generate_report": False}


db.users.insert(user)


db.users.create_index("username", unique = True)
