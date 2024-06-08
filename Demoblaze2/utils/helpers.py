import json

def read_login_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return [(entry["username"], entry["password"], entry["success"]) for entry in data]

def read_signup_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return [(entry["username"], entry["password"], entry["success"]) for entry in data]
