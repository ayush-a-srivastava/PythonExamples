#Here we are deleting the elements while iterating through the list

#In this case it actually delete the element from the list l
l = [10,20,13,43,12,70,50,60]
for i in range(len(l)-1,-1,-1):
    if l[i]>=50:
        del l[i]
        # l[i] = 20
print(l)

# But in this case it is deleting the reference of the list l ie. 'i' not the actual list
l1 = [10,20,13,43,12,70,50,60]
for i in l1:
    if i>=50:
        del i
print(l1)