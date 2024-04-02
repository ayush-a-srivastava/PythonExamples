#Here we are deleting the elements while iterating through the list

l = [10,20,13,43,12,70,50,60]
for i in range(len(l)-1,-1,-1):
    if l[i]>=50:
        del l[i]
print(l)