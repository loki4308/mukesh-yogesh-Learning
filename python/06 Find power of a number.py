# Find power of a number

def pow_of_num(base,power):
    if base == 0:
        return 0
    if power == 0:
        return 1
    return base ** power;

base = int(input("Enter a base number:"))
power = int(input("Enter a power number:"))
result = pow_of_num(base,power)
print(result)

# 2nd method without (**) operator

def pow_of_num(base,power):
    if base == 0:
        return 0
    if power == 0:
        return 1
    pow = 1
    for i in range(power):
        pow = pow * base
    return pow;


base = int(input("Enter a base number:"))
power = int(input("Enter a power number:"))
result = pow_of_num(base,power)
print(result)
