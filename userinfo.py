import json

def get_stored_username():
    """如果存储了用户名，就获取他"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """问候用户，并指出名字"""
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username()
        print(f"We'll remember you comer back, {username}!")

greet_user()

"""函数的分块，有利于维护"""
