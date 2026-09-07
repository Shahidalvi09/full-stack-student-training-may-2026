def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login Successful")
        return True

    else:
        print("worng username or password")
        return False