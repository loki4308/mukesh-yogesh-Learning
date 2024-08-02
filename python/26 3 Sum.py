# 3 Sum

# worst Case

def triplet_sum(arr,x,n):       # TC = O(N3) and SC = O(1)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == x:
                    return True
    return False

array = [12, 3, 4, 1, 6, 9]
sum = 24
n = len(array)
if triplet_sum(array,sum,n):
    print("Yes")
else:
    print("No")

# Better Case

def triplet__sum(arr,x,n):      # TC = O(N2) and SC = O(1)
    for i in range(0,n-2):
        left = i+1
        right = n-1
        while left < right:
            sum1 = arr[i] + arr[left] + arr[right]
            if sum1 == x:
                return True
            elif sum1 < x:
                left += 1
            else:
                right -= 1
    return False

array = [1, 2, 3, 4, 5]
sum = 9
n = len(array)
if triplet__sum(array,sum,n):
    print("Yes")
else:
    print("No")

