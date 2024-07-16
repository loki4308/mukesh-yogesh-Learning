# Reverse a number

def rev_num(n):
    if n < 10:
        return n;
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n //= 10
    return rev;


num = int(input("Enter a Number:"))
result = rev_num(num)
print("The reverse number of",num,"is",result)