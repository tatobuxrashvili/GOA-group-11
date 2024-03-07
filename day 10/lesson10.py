#ამ ფოტოს მიხედვიტ გააკეთეთ პროგრამა. (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა რეგისტრირებულ პაროლს, while ციკლის და  if else _ის გამოყენებით) 

password = "tatobuxrashvili"
while True:
    input_password = input("enter your password: ")

    if password == input_password:
        print("successfuly logged in")
        break
    else:
        print("incorrect password ")
        try_again = input("try_agein? (yes or no): ")
        if try_again == "no":
          break

        elif try_again != "yes":
            print("invalid input")
        



