# Sort an array of 0s , 1s and 2s

# brute force
# Merge Sort - TC = O(N log N) and SP = O(N)

def s_arr(arr,n):     # Time Complexity = O(2N) and Space Complexity = O(1)
    count0,count1,count2 = 0,0,0
    for i in range(n):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        elif arr[i] == 2:
            count2 += 1

    for i in range(0,count0):
        arr[i] = 0
    for i in range(count0,count0+count1):
        arr[i] = 1
    for i in range(count0+count1,n):
        arr[i] = 2

    return arr

arr1 = [0, 1, 2, 0, 1, 2]
n1 = len(arr1)
arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n2 = len(arr2)
print(s_arr(arr1,n1))
print(s_arr(arr2,n2))

# Optimal Case

def sort_array(arr,n):      # Time Complexity = O(N) and Space Complexity = O(1)
    low = 0
    mid = 0
    high = n-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1

    return arr


arr1 = [0, 1, 2, 0, 1, 2]
n1 = len(arr1)
arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n2 = len(arr2)
print(sort_array(arr1,n1))
print(sort_array(arr2,n2))