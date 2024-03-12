# Write a function that takes a string as input and returns True if first character of that string is "G".

# დაწერეთ ფუნქცია, რომელიც იღებს სტრიქონს შეყვანად და აბრუნებს True-ს, თუ ამ სტრიქონის პირველი სიმბოლოა "G".


while True:
    user_input = input("Enter text here: ")
    if user_input[0] == "g":
        print("True")
    else:
        print("false")