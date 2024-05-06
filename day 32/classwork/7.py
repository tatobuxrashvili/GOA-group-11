"""https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python"""

def camel_case(str):
    res_list = []
    
    str = str.split(" ")
    
    for word in str:
        res_list.append(word.capitalize())
        
    return "".join(res_list)