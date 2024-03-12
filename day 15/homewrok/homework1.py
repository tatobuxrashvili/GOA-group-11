# Write a program that takes asks user for number (use input).
# If number is even, print that number is even. Else print that number is not even,
# also print next even number, for example if input is 15, print 16.

# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ნომერს (გამოიყენეთ შეყვანა). თუ რიცხვი ლუწია, დაბეჭდეთ ეს რიცხვი ლუწი. 
# წინააღმდეგ შემთხვევაში დაბეჭდეთ ეს რიცხვი არ არის ლუწი, ასევე დაბეჭდეთ შემდეგი ლუწი რიცხვი, მაგალითად, თუ შეყვანილია 15, დაბეჭდეთ 16.


number = (int(input("what is your number: ")))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "not even")
















