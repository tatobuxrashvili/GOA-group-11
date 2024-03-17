# Write a function that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.

# დაწერეთ ფუნქცია, რომელიც ამოწმებს მოცემული რიცხვს მარტივია თუ არა (პირველ რიცხვს აქვს მხოლოდ ორი გამყოფი - გამყოფი) ამ ამოცანისთვის გამოიყენეთ for loop.


user_input = int(input("enter a number: "))

if user_input < 2:
    print("not a  number")
else:
    number = True
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            number = False
            break
