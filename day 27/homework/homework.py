#1
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

#2
def friend(names_list):
    friends = []
    
    for name in names_list:
        if len(name) == 4:
            friends.append(name)
    
    return friends

#3(rtuli gza)
def find_short(s):
    words_list = s.split(" ")
    
    min_length = len(words_list[0])
    
    for word in words_list:
        if min_length > len(word):
            min_length = len(word)
    
    return min_length
#martivi gza




