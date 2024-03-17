#Write a function that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5.
#დაწერეთ ფუნქცია, რომელიც მიიღებს სტრიქონების სიას შეყვანად და აბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ 5-ზე მეტი სიგრძის სტრიქონებს.

def filter(strings_list):
    filtered_list = []

    for word in strings_list:
        if len(word) > 5:
            filtered_list.append(word)
    
    return filtered_list

names = ["Nika","Luka","Gabrieli","Dato","Giorgi"]

print(filter(names))