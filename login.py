def login(username, password):
    # Check if the username and password are correct
    if username == "admin" and password == "password123":
        return True
    else:
        return False