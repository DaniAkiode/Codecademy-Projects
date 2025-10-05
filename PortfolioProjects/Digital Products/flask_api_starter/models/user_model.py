users = []

def get_all_users():
    return users

def add_user(user):
    users.append(user)
    return user

def update_user(index, new_data):
    if index < len(users):
        users[index] = new_data
        return users[index]
    return None 

def delete_user(index):
    if index < len(users):
        return users.pop(index)
    return None
