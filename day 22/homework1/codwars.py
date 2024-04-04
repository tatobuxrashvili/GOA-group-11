#1
def is_it_letter(s):
    return s.isalpha()

#2
def descending_order(num):
    num_str = str(num)
    sorted_str = ''.join(sorted(num_str, reverse=True))
    return int(sorted_str)

#3
def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letters in sentence:
        if letters in vowels:
            count += 1
    return count if count > 0 else 0 

#4
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

#5
def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i) % 2 == 0]

#6
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#7
def remove_exclamation_marks(s):
    return s.replace('!', '')

#8
def year_days(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} has 366 days"
    else:
        return f"{year} has 365 days"
    
#9
def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)

#10
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2