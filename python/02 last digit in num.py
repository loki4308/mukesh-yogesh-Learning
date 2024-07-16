# Find last digit in a number

def findfirstdigit(n):
    return n[0]
def findlastdigit(n,l):
    return n[l-1]

num = input("Enter a numbers:")
length = len(num)
print("The first digit of",num,"is",findfirstdigit(num))
print("The last digit of",num,"is",findlastdigit(num,length))

# output
# input = 12345
# first digit = 1
# second digit = 5