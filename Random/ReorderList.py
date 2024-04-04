l1 = [3,1,12,5,11,10,4]
l2 = [1,4,6,10]

new_l =[]
for i in l1:
    if i in l2:
        new_l.append(i)
print(new_l)