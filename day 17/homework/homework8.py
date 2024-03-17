#Write a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10. 
#დაწერეთ ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების ჩამონათვალს და აბრუნებს ყველა რიცხვის ჯამს, რომლებიც 10-ზე მეტია.

def sum_of_numbers(numbers):
    result = 0

    for num in numbers:
        if num > 10:
            result = result + num
    
    return result

print(sum_of_numbers([1,2,3,11,15,5]))