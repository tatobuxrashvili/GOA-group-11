#1
def countevennums(numbers):
    count = 0
    
    for num in numbers:
        if num % 2 == 0:
            count += 1
    
    return count

numbers = [1, 2, 3, 4, 5, 8, 9, 12]
print(countevennums(numbers))

#classwork
def my_replace(word, replace_char, input_char):
    changed_word = ''
    
    for char in word:
        if char == replace_char:
            changed_word = changed_word + input_char
        else:
            changed_word = changed_word + char
    
    return changed_word

print(my_replace("lukaak", "a", "d"))
def my_find(collection, value):
    for index in range(len(collection)):
        if collection[index] == value:
            return index
    return -1

print(my_find([1,2,3,4,5], 8))