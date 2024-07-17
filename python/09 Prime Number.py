# Prime number
def prime_num(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number:"))
result = prime_num(num)
if result == True:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")