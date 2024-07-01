person = {}

while True : 
    name  = input("Name  :  ")
    age = input("Age : ")
    person[name]= age

    another = input("Another Y/N")
    if another == "y" :
        continue
    else : 
        break

# person.item() # dict_items([('khun', '30'), ('win', '40')])

for (key, value) in person.items():
    print(f'{key} is {value} years old!')

    
# print(f'{key} is {value} years old!')
# Khun is 30 years old!
# kyaw is 40 years old!
# win is 50 years old!