from datetime import date, datetime

# Current Date
today = date.today()

print("Today's Date :", today)
print("Year         :", today.year)
print("Month        :", today.month)
print("Day          :", today.day)

# Date of Birth
dob = input("\nEnter Date of Birth (DD-MM-YYYY): ")

birth = datetime.strptime(dob, "%d-%m-%Y")

print("\nDate of Birth :", birth.date())
print("Birth Year    :", birth.year)
print("Birth Month   :", birth.month)
print("Birth Day     :", birth.day)
print("Day Name      :", birth.strftime("%A"))