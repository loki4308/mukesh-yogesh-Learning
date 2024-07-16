# Array Reverse

def arr_rev(arr):
    reversed_arr = arr[::-1]
    return reversed_arr

n = int(input("Enter an array size:"))
arr = []
for i in range(n):
    arr.append(input())
result = arr_rev(arr)
print(result)

# 2nd method

def arr_rev(arr,n):
    start = 0
    end = n-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

n = int(input("Enter an array size:"))
arr = []
for i in range(n):
    arr.append(input())
result = arr_rev(arr,n)
print(result)