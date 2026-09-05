from zoom1.auth1 import login
from zoom1.food  import order_food


while True:

    login()

    choice = input("Enter your choice: ")

    if choice == "6":
        print("thank you!")
        break

    order_food(choice)