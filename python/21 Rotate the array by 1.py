# Rotate the array by 1

# Optimal Case

def left_rotate_arr(arr,n):     # Time Complexity = O(N) and Space Complexity = O(1)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

def right_rotate_arr(arr,n):   # Time Complexity = O(N) and Space Complexity = O(1)
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

arr = [1,2,3,4,5]
n = len(arr)
print(left_rotate_arr(arr,n))
print(right_rotate_arr(arr,n))