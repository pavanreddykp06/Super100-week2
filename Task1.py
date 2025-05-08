users = [
    {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
    {"id": 2, "name": "Bob", "email": "bob@gmail.com"},
]

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def add_user(new_user):
    if get_user_by_id(new_user["id"]) is not None:
        print("User with this ID already exists.")
    else:
        users.append(new_user)
        print("User added successfully.")

def update_user(user_id, new_name=None, new_email=None):
    for user in users:
        if user["id"] == user_id:
            if new_name:
                user["name"] = new_name
            if new_email:
                user["email"] = new_email
            print("User updated successfully.")
            return
    print("User not found.")

def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print("User deleted successfully.")
            return
    print("User not found.")

print("Initial users:", users)
add_user({"id": 3, "name": "Charlie", "email": "charlie@gmail.com"})
update_user(2, new_email="bob.new@gmail.com")
print("User with ID 1:", get_user_by_id(1))
delete_user(1)
print("Final users:", users)
