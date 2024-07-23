# Find the maximum and minimum element in array

# brute force

def maximum_ele(arr,n):         # Time complexity = O(n log n)    # Space  complexity = O(1)
    for i in range(n):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[n-1]
def minimum_ele(arr,n):         # Time complexity = O(n log n)    # Space complexity = O(1)
    for i in range(n):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[0]

arr = [1,2,4,7,6,5]
n = len(arr)
print("The maximum element in array is",maximum_ele(arr,n))
print("The minimum element in array is",minimum_ele(arr,n))

# There is no better solution

# Optimal solution

def max_ele(arr,n):                 # Time Complexity = O(n)
    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def min_ele(arr,n):                 # Time Complexity = O(n)
    smallest = arr[0]
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr = [2,3,7,5,8,6,1,4]
n = len(arr)
print("The maximum element in array is",max_ele(arr,n))
print("The minimum element in array is",min_ele(arr,n))