num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
startnum = (min(num1, num2))
endnum = (max(num1, num2))

for i in range(startnum, endnum + 1):
    if i % 5 == 0:
      print(i)   


my_list = ["nika", "luka", "tato", "giorgi", "daviti"]

print(my_list[0:5:2])


number_lis = []

for i in range(0, 50 + 1):
    number_lis.append(i)

print(number_lis[0:25+ 1])    



######



