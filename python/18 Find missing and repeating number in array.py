# Find missing and repeating number in array

# Better Case
def miss_and_repeat_num(arr,n):  # Time Complexity = O(2N)  and Space Complexity = O(N)
    # create a hash array up to n+1
    hash = [0] * (n+1)

    # assign a value
    for num in arr:
        hash[num] += 1

    repeating,missing = -1,-1
    for i in range(1,n+1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i
    return repeating,missing


N = 4
arr = [1,2,3,2]
print(miss_and_repeat_num(arr,N))
arr1 = [1, 2, 3, 5]
n1 = 5
print(miss_and_repeat_num(arr1,n1))

# optimal case(using math method)
def missing_and_repeat_number(arr,n):  # TC = O(N) and SP = O(1)
    # x - repeating number
    # y - missing number
    # S - SN = x - y
    # S2 - S2N = x2 - y2
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1))  // 6
    S = 0
    S2 = 0
    for i in range(0,n):
        S += arr[i]
        S2 += arr[i] * arr[i]
    val1 = S - SN  # x -y
    val2 = S2 - S2N
    val2 = val2 // val1  # x + y
    x = (val1 + val2) // 2
    y = x - val1
    return x,y


arr1 = [4,3,6,2,1,1]
N1 = 6
print("The repeating and missing number is",missing_and_repeat_number(arr1,N1))
