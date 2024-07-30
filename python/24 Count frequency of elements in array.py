# Count frequency of elements in array

# create an array and inserting an element to the array
n = int(input("Enter array size:"))
arr = []
for i in range(n):
    arr.append(int(input()))

# Pre compute
hash = [0] * 13
for i in range(n):
    hash[arr[i]] += 1

Q = int(input("Enter no of search element:"))
while Q>0:
    num = int(input("Search element:"))
    print("The count frequency of",num," element is",hash[num])
    Q -= 1


