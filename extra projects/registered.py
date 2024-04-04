while True:

    print("1. sign up ")
    print("2. login up ")
    print("3. exit ")

    user_choice = int(input("please enter your choise:  "))


    if user_choice == 1:

        print("sign up page")
        registered_username =  input("please your name: ")
        registered_surname =  input("please your  surname: ")
        registered_password = input("please enter new password: ")
        registered_password2 = input("please enter Same password: ")
        
        if registered_password == registered_password2:
            print("You have successfully registered")
        else:
            print("You failed to register")

    elif user_choice == 2:
        print("login  page")
        username_input =  input("please enter your name: ")
        passsword_input = input("please enter your password: ")
    
        if username_input == registered_username and passsword_input == registered_password:
            print("You have successfully logged into your account")
            break
        else:
            print("please try again. you could not log in to your account")

    elif user_choice == 3:
        print("Thank you for using our program")
        break