#Write a function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'.
#დაწერეთ ფუნქცია, რომელიც მიიღებს სტრიქონების სიას შეყვანად და აბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ ასო "a"-ს დაწყებულ სტრიქონებს.

def filter_list(strings_list):
    filtered_list = []

    for word in strings_list:
        if word[0] == 'a':
            filtered_list.append(word)
    
    return filtered_list

words = ["apple", "anaconda", "anakomi", "python", "java", "javascript"]

print(filter_list(words))
