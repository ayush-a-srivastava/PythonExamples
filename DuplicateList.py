ar = [10,10,2,3,4,5,5]
new = []
dup=[]
for i in ar:
    if i not in new:
        new.append(i)
    else:
        dup.append(i)
print(new)
print(dup)


a = str(ar)
print(a)
print(type(a))