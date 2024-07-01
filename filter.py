nums = [1,2,3,4,5,6,7,8,9,10]

def filterList (num) :
    return (num%2)==0

evenNums = list(filter(filterList,nums))
print(evenNums)

# filter with comprehension way

nums_List = [num for num in nums if(num%2)==0]
print(nums_List)