import dashboard
user =['shahid','rihan','amir']



def login():
    id =input("enter your id:")
    for id in user:
        dashboard.user(id)


def ragister():
    id =input("enter tha new id:")
    
    user.append(id)
    print("welcome you are ragister:")

def menu():

    print("1.for tha login:")
    print("2.for tha ragister:")
    print("3.for tha exit:")
    while True:
     choice =int(input("enter your choice:"))

     if choice ==1:
        login()
     elif choice ==2:
        ragister()
     elif choice ==3:
        break
     else:
        print("invilide choice please try again:")


    print("thank you..!")

