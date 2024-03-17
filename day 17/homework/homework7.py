#Write a function that takes a list of strings as input and returns a new list containing the lengths of each string.
#დაწერეთ ფუნქცია, რომელიც იღებს სტრიქონების სიას შეყვანის სახით და აბრუნებს ახალ სიას, რომელიც შეიცავს თითოეული სტრიქონის სიგრძეს.

def strings_length(strings_list):
    length_list = []

    for word in strings_list:
        length_list.append(len(word))
    
    return length_list

print(strings_length(["luka","nika","gio","lolo"]))