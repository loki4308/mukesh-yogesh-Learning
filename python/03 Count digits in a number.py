# Count digits in a number

def count_digits(n):
    if n == 0:
        return 1;
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count;



num = int(input("Enter a Number:"))
result = count_digits(num)
print("The count digits of",num,"is",result)