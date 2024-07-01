names = ["Khun kyaw", "Khun Lay", "Khun Kham", "Khun Myo"]

for name in names : 
    if name == "Khun kyaw" : 
        print(f'{name} is developer.')
        break
        
    else : 
        print(f'{name} is friend.')


fruits = ["apple", "mango", "jeckfuit", "watermelon", "orange"]

for fruit in fruits : 
    print(f'{fruit.capitalize()} was orangic fruits from our farm!')


# while loop

num = 0 
while num < 10 : 
    if num > 5 :
        break
    if num % 2 == 0:
        print(f'{num}')
    num+=1