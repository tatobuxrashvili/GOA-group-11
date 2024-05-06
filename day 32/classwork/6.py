"""https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python"""


def to_weird_case(words):
    words = words.split(" ")
    
    res_list = []
    
    for word in words:
        modified_str = ""
        
        for i in range(len(word)):
            if i % 2 == 0:
                modified_str += word[i].upper()
            else:
                modified_str += word[i].lower()
            
        res_list.append(modified_str)
    
    return " ".join(res_list) 