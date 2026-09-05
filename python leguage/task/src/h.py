student_list = ["shahid", "aman", "aryan", "danish"]
password_list = ["1111", "2222", "3333", "4444"]



def register(student_list, password_list):

    name = input("Enter Student Name : ").strip().lower()

    if name == "":
        print("Name cannot be empty")
        return

    if not name.isalpha():
        print("Name should contain only letters")
        return

    if name in student_list:
        print("Student Already Registered")
        return

    password = input("Enter Password : ")

    if len(password) < 8:
        print("Password must be at least 8 characters")
        return

    if not any(ch.isupper() for ch in password):
        print("Password must contain Uppercase")
        return

    if not any(ch.islower() for ch in password):
        print("Password must contain Lowercase")
        return

    if not any(ch.isdigit() for ch in password):
        print("Password must contain Number")
        return

    student_list.append(name)
    password_list.append(password)

    print("Registration Successful")



def login(student_list, password_list):

    name = input("Enter Student Name : ").strip().lower()
    password = input("Enter Password : ")

    if name not in student_list:
        print("Student Not Found")
        return

    index = student_list.index(name)

    if password_list[index] == password:
        print("Login Successful")
    else:
        print("Wrong Password")



def delete(student_list, password_list):

    name = input("Enter Student Name : ").strip().lower()

    if name not in student_list:
        print("Student Not Found")
        return

    password = input("Enter Password : ")

    index = student_list.index(name)

    if password_list[index] == password:
        student_list.pop(index)
        password_list.pop(index)
        print("Account Deleted Successfully")
    else:
        print("Wrong Password")



def menu():

    while True:

        print("\n====== MENU ======")
        print("1. Register")
        print("2. Login")
        print("3. Delete")
        print("4. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            register(student_list, password_list)

        elif choice == "2":
            login(student_list, password_list)

        elif choice == "3":
            delete(student_list, password_list)

        elif choice == "4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


menu()