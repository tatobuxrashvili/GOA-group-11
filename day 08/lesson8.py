 #for loop'ით და while loop'ით ეცადეთ გამოიტანოთ რიცხვები 1'დან 100-ის ჩათვლით

counter = 0
while counter < 100:
    print(counter)
    counter += 1

for i in range(101):
    print(i)


#3) for ციკლის მეშვეობით შეკრიბეთ პირველი 10 რიცხვი

for i in range(1, 10):
    
      print(i)




#4) for ციკლის მეშვეობით გამოიტანეთ ლუწი რიცხვები 1'დან 20'ის ჩათვლით


for i in range(1, 21):
   if i % 2 == 0:
     print(i)