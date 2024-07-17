# Armstrong number
def check_armstrong_num(n,arm_num):
    if n == arm_num:
        return True
    else:
        return False
def power_cube(digit):
    return digit ** 3
def armstrong_num(num):
    n = num
    arm_num = 0
    digit = 0
    while n > 0:
        digit = n % 10
        arm_num = arm_num + power_cube(digit)
        n = n // 10
    return check_armstrong_num(num,arm_num)


num = int(input("Enter a number:"))
result = armstrong_num(num)
if result == True:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")