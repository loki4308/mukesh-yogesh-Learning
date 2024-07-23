# Find third largest element in array
import sys
# Brute force(Worst Case)

def largest(arr,n):           # Time Complexity = O(N log N + N)
    arr.sort()  # TC - O(N log N)
    large_ele = n-1
    sec_largest = n-2
    for i in range(n-3,0,-1):  # worst case  and TC = O(N)
        if arr[i] != large_ele and arr[i] != sec_largest:
            third_largest = arr[i]
            break
    return third_largest

arr = [1, 14, 2, 16, 10, 20]
n = len(arr)
print("The Largest element in array is",largest(arr,n))


# Better Case
def t_large(arr,n):     # Time Complexity = O(N+N+N) = O(3N)
    if n <3:
        return "Invalid Input"
    _largest = arr[0]
    for i in range(n):      # TC = O(N)
        if arr[i] > _largest:
            _largest = arr[i]
    S_largest = -1
    for i in range(n):      # TC = O(N)
        if arr[i] > S_largest and arr[i] != _largest:
            S_largest = arr[i]
    T_largest = -1
    for i in range(n):      # TC = O(N)
        if arr[i] > T_largest and arr[i] != S_largest and arr[i] != _largest:
            T_largest = arr[i]
    return T_largest

arr = [1, 14, 2, 16, 10, 20]
n = len(arr)
print("The Largest element in array is",t_large(arr,n))

# Optimal Case

def third_largest_element(arr,n):       # Time Complexity = O(N)
    first_largest = arr[0]
    second_largest = -sys.maxsize
    third_largest = -sys.maxsize
    for i in range(n):      # TC = O(N)
        if arr[i] > first_largest:
            third_largest = second_largest
            second_largest = first_largest
            first_largest = arr[i]
        elif arr[i] > second_largest:
            third_largest = second_largest
            second_largest = arr[i]
        elif arr[i] > third_largest:
            third_largest = arr[i]
    return third_largest

arr = [1, 14, 2, 16, 10, 20]
n = len(arr)
print("The Largest element in array is",third_largest_element(arr,n))
