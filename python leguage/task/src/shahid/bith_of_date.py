from datetime import date, datetime

# Today's Date
today = date.today()

print("Today's Date :", today)
print("Year         :", today.year)
print("Month        :", today.month)
print("Day          :", today.day)

# User DOB
dob = input("\nEnter Date of Birth (DD-MM-YYYY): ")

birth = datetime.strptime(dob, "%d-%m-%Y")

print("\n========== DATE OF BIRTH ==========")
print("Birth Date  :", birth.date())
print("Birth Year  :", birth.year)
print("Birth Month :", birth.month)
print("Birth Day   :", birth.day)
print("Day Name    :", birth.strftime("%A"))
print("Month Name  :", birth.strftime("%B"))
print("Week Number :", birth.strftime("%U"))
print("Day Number  :", birth.strftime("%j"))
print("Time        :", birth.time())