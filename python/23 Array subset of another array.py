# Array subset of another array
def arr_subnet(arr1,arr2):      # Time Complexity = O(N) and Space Complexity = O(1)
    # check whether the arr2 elements contains in arr1 elements 
    n2 = len(arr2)
    for i in range(n2):
        if arr2[i] not in arr1:
            return False
    return True

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
if arr_subnet(arr1,arr2):
    print("Yes")
else:
    print("No")