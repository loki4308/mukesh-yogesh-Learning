# Find pair with given sum
# Brute Force
def find_pair(arr,x,n):
    if n < 2:
        return False
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j] == x:
                print("index:",i,",",j)
                return True
    return False

arr = [0,-1,2,-3,1]
x = -2
n = len(arr)
if find_pair(arr,x,n):
    print("Yes")
else:
    print("No")

# Better Case

def find__pair(arr,x,n):        # TC = O(N) and SC = O(N)
    seen = set()        # hashing
    for num in arr:
        if x-num in seen:
            return True
        seen.add(num)
    return False

book = [4,1,2,3,1]
target = 5
n = len(book)
if find__pair(book,target,n):
    print("Yes")
else:
    print("No")

# Optimal Case

def find___pair(arr,x,n):       # TC = O(N log N) and SC = O(1)
    arr.sort()
    left = 0
    right = n-1
    while left < right:
        sum1 = arr[left] + arr[right]
        if sum1 == x:
            return True
        elif sum1 < x:
            left += 1
        else:
            right -= 1
    return False


arr = [5,8,2,6,11]
target = 14
n = len(arr)
if find___pair(arr,target,n):
    print("Yes")
else:
    print("No")