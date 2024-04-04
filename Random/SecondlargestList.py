arr = [10,3,19,14,2,13]
arr.sort()
print(arr[-2])


sub = [x for x in arr if x<max(arr)]
print(max(sub))