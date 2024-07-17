# Square root of a number
import math
def square_root(n):
    return n ** 0.5

num = int(input("Enter a number:"))
result = square_root(num)
print("The square root of",num,"(in floating or decimal is",result)
print("The square root of",num,"(in integer is",math.floor(result))
