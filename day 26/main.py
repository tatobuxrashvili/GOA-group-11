def my_range(start, end, step):
    numbers = []

    while start < end:
        numbers.append(start)
        start = start + step
    
    return numbers

print(my_range(0,10 + 1,2))


#დავალება: შექმენით პროგრამა, სადაც ბოლოდან პირველ ოთხის ჯერად რიცხვს გამოიტანთ სიიდან. მაგ სიაში კი 10-იდან 50-ის ჩათვლით უნდა იყოს რიცხვები
numbers = []

for i in range(10, 50 + 1):
    numbers.append(i)

# Second Part

def func(numbers):
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] % 4 == 0:
            return numbers[index]

print(func(numbers))


#დავალება: შექმენით range-ის მსგავსი ფუნქცია, სადაც მესამე არგუმენტი იქნება მომხმარებლის მიერ შეტანილი. აგრეთვე კომენტარით აღწერეთ return

 









# დავალება2: შექმენით ფუნქცია სახელად filter, მისი პირველი პარამეტრი იქნება კოლექცია, მეორე კი მნიშვნელობა.
# თქვენი დავალებაა, რომ კოლექციიდან ამოიღოთ ეგ კონკტეტული მნიშვნელობები და დააბრუნოთ ის