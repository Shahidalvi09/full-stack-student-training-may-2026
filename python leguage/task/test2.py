import json
from datetime import datetime, timedelta

file = "tables.json"


def create_tables():

    tables = []

    for i in range(8):

        table = {
            "table": 101 + i,
            "size": "",
            "customer": "",
            "date": "",
            "time": "",
            "booked_at": "",
            "hours": 0
        }

        if i < 2:
            table["size"] = "Big"
        elif i < 5:
            table["size"] = "Medium"
        else:
            table["size"] = "Small"

        tables.append(table)

    data = {"tables": tables}

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def load_data():

    try:

        with open(file, "r") as f:
            return json.load(f)

    except FileNotFoundError:

        create_tables()

        with open(file, "r") as f:
            return json.load(f)


def save_data(data):

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


class Book:

    def book_table(self):

        data = load_data()

        print("\nAvailable Tables")

        for table in data["tables"]:

            if table["customer"] == "":
                print(table["table"], "-", table["size"], "- Available")
            else:
                print(table["table"], "-", table["size"], "- Booked")

        table_no = int(input("\nTable: "))

        for table in data["tables"]:

            if table["table"] == table_no:

                if table["customer"] != "":
                    print("Table already booked")
                    return

                name = input("Name: ")
                date = input("Date: ")
                time = input("Time: ")
                hours = float(input("Hours: "))

                table["customer"] = name
                table["date"] = date
                table["time"] = time
                table["booked_at"] = datetime.now().isoformat()
                table["hours"] = hours

                save_data(data)

                print("\n--------------------------")
                print("    Booking Successful")
                print("--------------------------")
                print("Table:", table["table"])
                print("Name:", table["customer"])
                print("Date:", table["date"])
                print("Time:", table["time"])
                print("Hours:", table["hours"])
                print("--------------------------")

                return

        print("Table not found")


class Update:

    def update_table(self):

        data = load_data()

        table_no = int(input("Table: "))

        for table in data["tables"]:

            if table["table"] == table_no:

                if table["customer"] == "":
                    print("Table is empty")
                    return

                table["customer"] = input("Name: ")
                table["date"] = input("Date: ")
                table["time"] = input("Time: ")
                table["hours"] = float(input("Hours: "))
                table["booked_at"] = datetime.now().isoformat()

                save_data(data)

                print("Booking updated successfully")
                return

        print("Table not found")


class Delete:

    def delete_table(self):

        data = load_data()

        table_no = int(input("Table: "))

        for table in data["tables"]:

            if table["table"] == table_no:

                if table["customer"] == "":
                    print("Table is already empty")
                    return

                table["customer"] = ""
                table["date"] = ""
                table["time"] = ""
                table["booked_at"] = ""
                table["hours"] = 0

                save_data(data)

                print("Booking deleted successfully")
                return

        print("Table not found")


class Display:

    def show_tables(self):

        data = load_data()

        print("\n========== TABLES ==========")

        for table in data["tables"]:

            if table["customer"] == "":
                status = "Available"
            else:
                status = "Booked"

            print("\nTable:", table["table"])
            print("Size:", table["size"])
            print("Name:", table["customer"])
            print("Date:", table["date"])
            print("Time:", table["time"])
            print("Hours:", table["hours"])
            print("Status:", status)


def check_time():

    data = load_data()
    change = False

    for table in data["tables"]:

        if table["customer"] != "" and table["booked_at"] != "":

            start = datetime.fromisoformat(table["booked_at"])

            end = start + timedelta(hours=table["hours"])

            if datetime.now() >= end:

                table["customer"] = ""
                table["date"] = ""
                table["time"] = ""
                table["booked_at"] = ""
                table["hours"] = 0

                change = True

    if change:
        save_data(data)


def main():

    load_data()

    while True:

        check_time()

        print("\n==========================")
        print("     HOTEL MANAGEMENT")
        print("==========================")
        print("1. Book")
        print("2. Show")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        print("==========================")

        choice = input("Choice: ")

        if choice == "1":

            Book().book_table()

        elif choice == "2":

            Display().show_tables()

        elif choice == "3":

            Update().update_table()

        elif choice == "4":

            Delete().delete_table()

        elif choice == "5":

            print("Thank you")
            break

        else:

            print("Wrong choice")


main()