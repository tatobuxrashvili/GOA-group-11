pin = 1234
authorized = False

while authorized != True:
    user_input = int(input("please enter your pincode: "))

    if user_input == pin:
      print("access Granted")
      authorized = True
    else:
         print("please try again")




