# Print all divisors of a number

def divisors_of_num(n):
    divisors = []
    for i in range(1,(n // 2)+1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors


num = int(input("Enter a number:"))
result = divisors_of_num(num)
print(result)
