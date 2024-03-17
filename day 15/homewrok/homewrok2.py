# Create a while loop that asks the user to enter a password.
#  Keep asking until they enter the correct password "Goa best". 
#  Also print the count of incorrect passwords.

# შექმენით while ციკლი, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. 
# განაგრძეთ კითხვა, სანამ არ შეიყვანენ სწორ პაროლს "Goa best". 
# ასევე დაბეჭდეთ არასწორი პაროლების რაოდენობა.

correct_password = "goa best"
incorrect_password = -3

while True:
    password = input("Enter the password: ")
    incorrect_password += 1

    if password == correct_password:
        print("Correct password! Access.")
        break
    else:
        print("Incorrect password.")


