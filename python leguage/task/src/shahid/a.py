from datetime import date,datetime

date = datetime.now()
print("========================================")
print("             date and time              ")
print("========================================")
print(datetime.now())


today = date.today()
print("========================================")
print("             day and year              ")
print("========================================")
print("Year :", today.year)
print("Month:", today.month)
print("Day  :", today.day)
print("day-name :",today.strftime("%A"))


