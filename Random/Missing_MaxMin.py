arr = [1, 2, 10, 9, 11]
min = arr[0]
max = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print("Maximum: ", max, "\nMinimum: ", min)
# new_l = []
# for j in range(min, max + 1):
#     if j not in arr:
#         new_l.append(j)

res = [num for num in range(min,max+1) if num not in arr]
print(res)

print("Missing numbers are: ",res)
