nums =  [1,2,3,4,5,6,7,8,9,10]

# map function normal way
def mapFunction ( num ) :
    return num * 2

nums_list = list(map(mapFunction, nums))
nums_val =list(map(mapFunction, nums))

print(nums_list)
print(nums_val)

# map function with comprehension way

nums_lists = [num*2 for num in nums]

print(nums_lists)