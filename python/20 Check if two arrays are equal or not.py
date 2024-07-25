# Check if two arrays are equal or not

# Brute Force(Worst Case)

def check_arr(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 != n2:
        return False

    arr1.sort()
    arr2.sort()

    for i in range(n1):
        if arr1[i] == arr2[i]:
            return True
        else:
            return False


arr1 = [1, 2, 5, 4, 0, 2, 1]
arr2 = [2, 4, 5, 0, 1, 1, 2]
if check_arr(arr1,arr2):
    print("Yes")
else:
    print("No")