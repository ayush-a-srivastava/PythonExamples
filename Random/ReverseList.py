l = [10,23,34,2,12,25,6]
new_l =[]
for i in range(len(l)-1,-1,-1):
    new_l.append(l[i])
print(new_l)


print("############ Reversing a list and converting to string")
arr = [1, 2, 0, 4, 3, 0, 5, 0]
res = ' '.join(map(str,arr[::-1]))
print(res)
l1 = []
if not l1:
    print("empty")
else:
    print("Not empty")
