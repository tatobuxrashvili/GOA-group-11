# Using for loop, ask user for number. Then create a list which will have even 
#numbers in next range: from 0 to user's number. At last, print out whole list. 
# loop-ის გამოყენებით, სთხოვეთ მომხმარებელს ნომერი. შემდეგ შექმენით სია, 
# რომელსაც ექნება ლუწი რიცხვები შემდეგ დიაპაზონში: 0-დან მომხმარებლის ნომრამდე. 
# და ბოლოს, ამობეჭდეთ მთელი სია.


number = int(input("enter number: "))
list = []

for i in range(0, number + 1):
    list.append(i)
print(list)