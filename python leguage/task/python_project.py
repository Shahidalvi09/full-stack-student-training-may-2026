import os
import re
from datetime import datetime



os.makedirs("logs", exist_ok=True)


def write_log(message):
    with open("logs/system.log", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {message}\n")




class ValidationError(Exception):
    pass




def validate_student(student):

    if len(student) != 6:
        raise ValidationError("6 fields required")

    student_id, name, age, email, address, country = student

    
    if not student_id.isdigit():
        raise ValidationError(
            "Invalid ID! ID me sirf number hona chahiye."
        )

    
    if not name.replace(" ", "").isalpha():
        raise ValidationError(
            "Invalid Name! Name me sirf letters hone chahiye."
        )

    
    if not age.isdigit():
        raise ValidationError(
            "Invalid Age! Age me sirf number hona chahiye."
        )

    age = int(age)

    if age < 5 or age > 100:
        raise ValidationError(
            "Invalid Age! Age 5 se 100 ke beech honi chahiye."
        )

    
    if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
        raise ValidationError(
            "Invalid Email! Email sahi format me hona chahiye."
        )

    
    if address.strip() == "":
        raise ValidationError(
            "Invalid Address! Address empty nahi hona chahiye."
        )

    
    if not country.replace(" ", "").isalpha():
        raise ValidationError(
            "Invalid Country! Country me sirf letters hone chahiye."
        )

    return True



def input_student():

    
    while True:
        student_id = input("Enter ID: ")

        try:
            validate_student(
                [student_id, "Test", "20",
                 "test@gmail.com", "Test Address", "India"]
            )
            break
        except ValidationError as e:
            print(e)

    
    while True:
        name = input("Enter Name: ")

        try:
            validate_student(
                [student_id, name, "20",
                 "test@gmail.com", "Test Address", "India"]
            )
            break
        except ValidationError as e:
            print(e)

    
    while True:
        age = input("Enter Age: ")

        try:
            validate_student(
                [student_id, name, age,
                 "test@gmail.com", "Test Address", "India"]
            )
            break
        except ValidationError as e:
            print(e)

    
    while True:
        email = input("Enter Email: ")

        try:
            validate_student(
                [student_id, name, age,
                 email, "Test Address", "India"]
            )
            break
        except ValidationError as e:
            print(e)

    
    while True:
        address = input("Enter Address: ")

        try:
            validate_student(
                [student_id, name, age,
                 email, address, "India"]
            )
            break
        except ValidationError as e:
            print(e)

    
    while True:
        country = input("Enter Country: ")

        try:
            validate_student(
                [student_id, name, age,
                 email, address, country]
            )
            break
        except ValidationError as e:
            print(e)

    return [
        student_id,
        name,
        age,
        email,
        address,
        country
    ]


print("---------------- SAVE DATA ----------------")

def save_student(student):

    with open("students.txt", "a") as file:
        file.write(",".join(student) + "\n")

    write_log("Student data saved successfully.")



def process_students():

    valid_students = []

    try:

        with open("students.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                student = line.split(",")

                try:

                    validate_student(student)

                    valid_students.append(student)

                    write_log(
                        "Student validation successful."
                    )

                except ValidationError as e:

                    print("Invalid student:", e)

                    write_log(
                        "Student validation failed: " + str(e)
                    )

    except FileNotFoundError:

        print("students.txt file not found!")
        write_log("students.txt file not found.")
        return

 
    with open("students_output.txt", "w") as file:

        for student in valid_students:

            student_id, name, age, email, address, country = student

            file.write(f"ID: {student_id} | ")
            file.write(f"Name: {name} | ")
            file.write(f"Age: {age}\n")

            file.write(f"Email: {email}\n")
            file.write(f"Location: {address}, {country}\n\n")

    print("\nValid student data saved in students_output.txt")

    write_log("Output file created successfully.")




def main():

    while True:

        print("\n===== STUDENT REGISTRATION SYSTEM =====")
        print("1. Register Student")
        print("2. Process students.txt")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            student = input_student()

            save_student(student)

            print("\nStudent registered successfully!")

        elif choice == "2":

            process_students()

        elif choice == "3":

            print("Program closed.")
            write_log("Program closed.")
            break

        else:

            print("Invalid choice! 1, 2 ya 3 enter karo.")




main()