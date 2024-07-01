def main (): 
    x = int (input("What's x? "))
    print("X squared is", square_with_multi(x))
    print("X squared with power is", square_with_power(x))
    print("X squared with pow is", square_with_pow(x))

def square_with_multi(n): 
    return n * n


def square_with_power(num2):
    return num2 ** 2

def  square_with_pow(num):
    return pow(num, 2)

main()