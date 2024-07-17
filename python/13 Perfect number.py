# Perfect number

def check_perfect_num(num,prft_num):
    if num == prft_num:
        return True
    else:
        return False
def divisors(n):
    div = []
    for i in range(1,int(n // 2)+1):
        if n % i == 0:
            div.append(i)
    return div
def perfect_num(num):
    prft_num = 0
    for divisor in divisors(num):
        prft_num += divisor
    return check_perfect_num(num,prft_num)

num = int(input("Enter a number:"))
if perfect_num(num):
    print(num,"is a Perfect number")
else:
    print(num,"is not a Perfect number")