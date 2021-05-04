import json
import hashlib
import os
import sys
import getpass
import base64

ALL_PASSWORDS = 'save.json'


def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return [base64.b64encode(salt).decode('utf-8'), base64.b64encode(hashed).decode('utf-8')]

def load_json():
    with open(ALL_PASSWORDS, 'r') as f:
        data = json.load(f)
    return data

def update_json(user):
    data = load_json()
    with open(ALL_PASSWORDS, 'w') as f:
        data.update(user)
        json.dump(data, f, indent = 4)

def check_duplicate(username):
    data = load_json()
    if username in data:
        return 1
    return 0
        
def add(username, password):

    if check_duplicate(username):
        return 0

    hashed = hash_password(password)
    user = {username : [hashed[0], hashed[1], 0]}
    update_json(user)
    return 1


def forcepass(username):
    with open(ALL_PASSWORDS, 'r') as f:
        data = json.load(f)
    
    if not check_duplicate(username):
        return 0
    
    user = data[username]
    user[2] = 1
    user = {username : user}    
    update_json(user)
    return 1

def delete(username):
    data = load_json()
    data.pop(username, None)
    
    with open(ALL_PASSWORDS, 'w') as f:
        json.dump(data, f, indent = 4)

def passwd(username, new_password):
    data = load_json()
    
    hashed = hash_password(new_password)

    user = {username : [hashed[0], hashed[1], data[username][2]]}
    update_json(user)



def main():
    if not os.path.isfile(ALL_PASSWORDS):
            with open(ALL_PASSWORDS, 'w') as f:
                f.write(json.dumps({}))

    username = sys.argv[2]
    if sys.argv[1] == 'add':
        
        password = input()
        repeat_password = input()
        
        if password != repeat_password:
            print('User add failed. Password mismatch.')
        else:
            if add(username, password):
                print('User ' + username + ' succesfully added.')
            else: print('User already added.')

    
    elif sys.argv[1] == 'passwd':
        password = input()
        repeat_password = input()

        if password != repeat_password:
            print('Password change failed. Password mismatch.')
        else:
            passwd(username, password)
            print('Password change succsesful.')

    elif sys.argv[1] == 'forcepass':
        if forcepass(username):
            print('User be forced to change the password on the next login.')
        else: print('Error. User does not exist.')
    elif sys.argv[1] == 'del':
        delete(username)
        print('User succesfully deleted.')

        

if __name__ == '__main__':
    main()