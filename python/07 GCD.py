# GCD or HCF

def gcd(n1,n2):
    if n1 == n2:
        return n1
    if n1 > n2:
        while n2 > 0:
            n1 , n2 = n2 , n1 % n2
        return n1
    else:
        while n1 > 0:
            n2 , n1 = n1 , n2 % n1
        return n2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
result = gcd(num1,num2)
print(result)