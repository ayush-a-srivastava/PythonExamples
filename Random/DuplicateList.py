ar = [10,10,2,3,4,5,55,10,5,10]
new_l = []
dup_l = []
for i in ar:
    if i not in new_l:
        new_l.append(i)
    else:
        dup_l.append(i)
print(new_l)
print(dup_l)
