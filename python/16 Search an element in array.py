# Search an element in array

# Optimal Case
def search_ele(arr,x):      # Time Complexity = O(N)
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1



arr = [10, 8, 30, 4, 5]
x1 = 5
x2 = 6
print(search_ele(arr,x1))
print(search_ele(arr,x2))