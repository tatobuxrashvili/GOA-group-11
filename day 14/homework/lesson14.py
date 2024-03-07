#დავალება1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით 
#(ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
print(number)


#დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.

even_number = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_number)

#დავალება3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი 
#(დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.

my_arrary = []

for number in range(50, 101):
    my_arrary.append(number)

    print(my_arrary[-5:])



# დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, 
# შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის, ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ.
#  ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
startnum = (min(num1, num2))
endnum = max(num1, num2)

for i in range(startnum, endnum + 1):
    if i % 5 == 0:
      print(i)   



#დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. 
#მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.

name_array = []
age = int(input("enter your age: "))

if age > 18:
   name = input("enter your name: ")
   name_array.append(name)
   print("name in the array:", my_arrary)
else:
    print("you are not eligible to provide a name" )





