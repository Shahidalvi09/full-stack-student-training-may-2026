student_list = []
password_list = []


def register(student_list, password_list):

    name = input("Enter Student Name : ")

    if name in student_list:
        print("Student Already Registered")
        return

    password = input("Enter Password : ")

    if not any(i.isupper() for i in password):
        print("Password must contain Uppercase")
        return

    if not any(i.islower() for i in password):
        print("Password must contain Lowercase")
        return

    if not any(i.isdigit() for i in password):
        print("Password must contain Number")
        return

    student_list.append(name)
    password_list.append(password)

    print("Registration Successful")


def login(student_list, password_list):

    name = input("Enter Student Name : ")
    password = input("Enter Password : ")

    if name in student_list:
        index = student_list.index(name)

        if password_list[index] == password:
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Student Not Found")


def delete(student_list, password_list):

    name = input("Enter Student Name : ")

    if name in student_list:
        index = student_list.index(name)
        student_list.pop(index)
        password_list.pop(index)
        print("Account Deleted")
    else:
        print("Student Not Found")


while True:

    print("\n===== MENU =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("4. Delete")

    choice = input("Enter Choice : ")

    if choice == "1":
        register(student_list, password_list)

    elif choice == "2":
        login(student_list, password_list)

    elif choice == "3":
        print("Thank You")
        break

    elif choice == "4":
        delete(student_list, password_list)

    else:
        print("Enter Correct Choice")