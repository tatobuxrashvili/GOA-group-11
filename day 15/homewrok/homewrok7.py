# Implement a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding operation.
# Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.



# განახორციელეთ მარტივი კალკულატორი, რომელიც იღებს ორ რიცხვს და ოპერატორს (+, -, *, /)
# როგორც შეყვანილი მომხმარებლისგან და ასრულებს შესაბამის ოპერაციას. ბონუს დავალება თუ გინდა, 
# არ არის საჭირო - დაამატე ხარისხი (ქარი), ამისთვის გამოიყენეთ ** ოპერატორი.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
 
choice = int(input(f"1 for addition, 2 for subtraction, 3 for multiplication, 4 for division and 5 to find {num1} to the power of {num2}:"))
print(choice)
 
if choice == 1:
    print(num1 + num2)
 
elif choice == 2:
    print(num1 - num2)
 
elif choice == 3:
    print(num1 * num2)
 
elif choice == 4:
    print(num1 / num2)
 
elif choice == 5:
    print(num1 ** num2)
 
else:
    print("Invalid input.")