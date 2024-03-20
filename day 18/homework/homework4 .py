# შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში.
# შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.
# Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ. 


def even_indexes(lastname):
    char_list = []
    even_index_chars = []

    for char in lastname:
        char_list.append(char)
    
    for index in range(len(char_list)):
        if index % 2 == 0:
            even_index_chars.append(char_list[index])
    
    return even_index_chars


lastname = input("Please enter lastname: ")

print(even_indexes(lastname))



