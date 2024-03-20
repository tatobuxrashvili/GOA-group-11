def no_space(x):
    result = ""

    for char in x:
        if char != " ":
            result = result + char

    return result  

print(no_space("r t  f  5 6 7   573 45  g s ge"))       
  