prices_list = [200, 300,400,500, 1000]

double_price_list = []

# Normal Way to append

# for price in prices_list : 
#     double_price_list.append(price*2)

# print("Printing with normal way: ",double_price_list)

#  Comprehension Way to append

# double_price_list = [ price*2 for price in prices_list]

double_price_list = [price*2 for price in prices_list if (price%200)==0] 

print("Printing with comprehensive way : ",double_price_list)