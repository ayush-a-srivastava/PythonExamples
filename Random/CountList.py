ar = [10,10,2,3,4,5,5]
sub = 5
c = 0
d = {}
for i in ar:
    d[i] = ar.count(i)
print(d)
for i in ar:
    if i == sub:
        c+=1
print(c)
