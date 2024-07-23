# Find missing number in array

# Optimal Case
def missing_num(arr,n):     # Time Complexity = O(N)
    for i in range(1,n+1):
        if i not in arr:
            return i

arr1 = [1, 2, 4, 6, 3, 7, 8]
N1 = 8
arr2 = [1, 2, 3, 5]
N2 = 5
print("The missing number is",missing_num(arr1,N1))
print("The missing number is",missing_num(arr2,N2))
