#1
def minimum(arr):
    #your code here...
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low
def maximum(arr):
    #...and here
    low = arr[0]
    for i in arr[1:]:
        if i > low:
            low = i
    return low

#2
def greet(name):
    return f'Hello, {name} how are you doing today?'

#3
def double_char(s):
    return ''.join(c* 2 for c in s)

#4
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    m = []
    for i in birds:
        if i not in geese:
            m.append(i)
    return(m)

