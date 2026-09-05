def register():
    print("=====================================")
    print("         REGISTERATION               ")
    print("=====================================")

    user_id = input("enter your id :")
    user_password = input("enter your password :")

    if user_id == "101" and  user_password == "1234":
     print("register successfully")
     return True
    else:
     print("worng id and password :")
    return False

def login():
  print("=========================================")
  print("                 LOGIN                   ")
  print("=========================================")

  user_id = input("enter your id :")
  user_password =input("enter your password :")

  if user_id == "101" and user_password == "1234":
    print("login successsfull ")
    return True
  else:
    print("worng id and password ")
    return False