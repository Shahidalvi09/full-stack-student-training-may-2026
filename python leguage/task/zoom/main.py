from authentication import register,login
from dashboard import dashboard
from meeting import meeting


while True:

    print("\n========== MAIN MENU ==========")
    print("1. Registration")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
          register()

    elif choice == "2":

        if login():

            while True:

                dashboard()

                choice2 = input("Enter your choice: ")

                if choice2 == "1":
                    meeting()

                elif choice2 == "2":
                    print("Logout")
                    break

                else:
                    print("Wrong Choice")

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Wrong Choice")