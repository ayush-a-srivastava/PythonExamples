ar = [10,10,2,3,4,5,55,10,5,10,1,10]
without_dup_l = []
dup_l = []
for i in ar:
    if i not in without_dup_l:
        without_dup_l.append(i)
    else:
        dup_l.append(i)
print("Without Duplicates: ", without_dup_l)
print("With Duplicates: ",dup_l)
