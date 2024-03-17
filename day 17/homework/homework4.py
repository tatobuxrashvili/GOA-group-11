#Write a function that takes a list of numbers as input and returns the largest number in the list.
#დაწერეთ ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების სიას და აბრუნებს სიაში ყველაზე დიდ რიცხვს.

def largest_number(numbers):
    max_number = numbers[0]

    for num in numbers:
        if max_number < num:
            max_number = num
    
    return max_number

numbers = [4,3,5,2,1]

print(largest_number(numbers))