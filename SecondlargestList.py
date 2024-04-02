arr = [10,3,19,14,2,13]
arr.sort()
print(arr[-2])

for i in arr:
    if i<max(arr):
        second = i
print(second)