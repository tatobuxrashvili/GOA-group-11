
# Manual Sum Function: Create a function called manual_sum that iterates over list and adds their sum in a variable, then returns variable. Use for loop for this task

def manual_sum(number_list, starting_value = 0):
    result = starting_value

    for num in number_list:
        result = result + num
    
    return result


print(manual_sum([1,2,3,4,5]))



def manual_sum(number_list):
    result = 0

    for num in number_list:
        result = result + num
    
    return result


# 2. Manual Max Function: Define a function named manual_max that iterates through list, updating a variable with the maximum value, 
# then returns the maximum value found. Use for loop for this task.

def manual_max(number_list):
    max_value = number_list[0]

    for num in number_list:
        if max_value < num:
            max_value = num
    
    return max_value

print(manual_max([1,2,3,4,5]))



# 3. Manual Min Function: Define a function named manual_min that iterates through list, updating a variable 
# with the minimum value, then returns the minimum value found. Use for loop for this task.


def manual_min(number_list):
    min_value = number_list[0]

    for num in number_list:
        if min_value > num:
            min_value = num
    
    return min_value

print(manual_min([1,2,3,4,5]))


# 4. Manual Len Function: Develop a function named manual_len that iterates through list, counting each element,
# and returns the count as the length of the list. Use for loop for this task.


def manual_len(collection):
    count = 0

    for _ in collection:
        count = count + 1
    
    return count

print(manual_len([1,2,3,4,5]))
print(manual_len("tato"))
print(manual_len(range(10)))







