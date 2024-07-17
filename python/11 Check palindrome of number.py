# Check palindrome of number
def check_palindrome(num,rev):
    if num == rev:
        return True
    else:
        return False

def palindrome(num):
    n = num
    if n < 10:
        return n;
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n //= 10
    return check_palindrome(num,rev)


num = int(input("Enter a Number:"))
if palindrome(num):
    print(num,"is a Palindrome")
else:
    print(num,"is not a Palindrome")
