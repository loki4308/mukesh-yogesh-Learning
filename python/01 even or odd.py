# Find even or odd

def EvenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number:"))
result = EvenOrOdd(num)
print(result)