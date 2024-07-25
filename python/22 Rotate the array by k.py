# Rotate the array by k

# Brute Force
def rotate_arr(arr,d,n):        # Time Complexity = O(N + d)  and Space Complexity = O(d)
    temp = arr[0:d]             # TC = O(d)
    for i in range(d,n):        # TC = O(N-d)
        arr[i-d] = arr[i]

    for i in range(n-d,n):      # TC = O(d)
        arr[i] = temp[i - (n-d)]

    return arr

arr = [1,2,3,4,5,6,7]
d = 3
n = len(arr)
print(rotate_arr(arr,d,n))

# Optimal Case
"""
reverse(a,a+d)      - TC = O(d)
reverse(a+d,a+n)    - TC = O(n-d)
reverse(a,a+n)      - Tc = O(n)

Time Complexity = O(2N) and Space Complexity = O(1)
"""

def rot_arr(arr,d,n):
    start1 = 0
    end1 = d-1
    while start1 < end1:
        arr[start1],arr[end1] = arr[end1],arr[start1]
        start1 += 1
        end1 -= 1
    start2 = d
    end2 = n-1
    while start2 < end2:
        arr[start2],arr[end2] = arr[end2],arr[start2]
        start2 += 1
        end2 -= 1

    arr.reverse()
    return arr

arr = [1,2,3,4,5,6,7]
d = 3
n = len(arr)
print(rot_arr(arr,d,n))

