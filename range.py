nums = [ 0, 1,  2, 3, 4, 5, 6 ]

for num in nums : 
    print( num )


print ("Divided data lists .")
 
# range ( 0, 3, option) with 3 parametor or variable three para is option

for num in range(0, 20) : # 0 is default data in python
    print(num)

for num in range(0, 20 , 3) : # 3  is option data in python
    print(num)


#  lists of lenght = len

pizzas = [ "chicken", "pork", "seafood", "cheese", "Beef"]

print("Pizzas total types :",len(pizzas))

for num in range(len(pizzas)):
    print(pizzas[num])