l = [3,4,5,6,7]
size = len(l)

temp = l[0]
l[0] = l[size - 1]
l[size-1] = temp

print(l)
