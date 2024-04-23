l =[2,12,4,1,23,11]
print("Before Sorting: ",l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
            # temp=l[i]
            # l[i] = l[j]
            # l[j] = temp
print("After Sorting: ",l)
print("Second Largest is:", l[-2])