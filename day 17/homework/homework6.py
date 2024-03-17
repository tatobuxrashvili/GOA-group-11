#Write a function that takes a list of numbers as input and returns a new list containing the square of each number.
#დაწერეთ ფუნქცია, რომელიც იღებს რიცხვების სიას შეყვანის სახით და აბრუნებს ახალ სიას, რომელიც შეიცავს თითოეული რიცხვის კვადრატს.

def squared_numbers(numbers):
    squared_numbers_list = []

    for num in numbers:
        squared_numbers_list.append(num * num)
    
    return squared_numbers_list

print(squared_numbers([1,2,3,4,5]))