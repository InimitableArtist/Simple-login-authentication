import sys
import getpass
import hashlib
from usermgmt import load_json, check_duplicate, passwd, update_json
import base64

def change_password(username):
    new_password = getpass.getpass('New password: ')
    repeat_new_password = getpass.getpass('Repeat new password: ')

    if new_password != repeat_new_password:
        print('Password change failed. Password mismatch.')
        return 0

    passwd(username, new_password)
    data = load_json()
    data[username][2] = 0
    user = {username : data[username]}
    update_json(user)
    return 1


def login(username, password):
    if not check_duplicate(username):
        return 0
    data = load_json()

    real_hashed_key = base64.b64decode(data[username][1])
    salt = base64.b64decode(data[username][0])
    new_hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if real_hashed_key != new_hashed:
        return 0

    if data[username][2] == 1:
        change_password(username)

    return 1

def main():
    username = sys.argv[1]
    password = getpass.getpass('Password: ')
    log = login(username, password)
    while not log:
        print('Username or password incorrect.')
        password = getpass.getpass('Password: ')
        log = login(username, password)
    
    print('Login succesful.')


if __name__ == '__main__':
    main()