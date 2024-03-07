number = int(input("what is your number: "))
if number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
else:
    print(number)