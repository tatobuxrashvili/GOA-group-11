# Ask user for five names (use input five times). Add all of them in one list and print only first three names.

# სთხოვეთ მომხმარებელს ხუთი სახელი (გამოიყენეთ შეყვანა ხუთჯერ). დაამატეთ ყველა მათგანი ერთ სიაში და დაბეჭდეთ მხოლოდ პირველი სამი სახელი.

names_list = []

for i in range(5):
    name = input("enter your full name: ")
    names_list.append(name)

print("first three names: ", names_list[:3])

