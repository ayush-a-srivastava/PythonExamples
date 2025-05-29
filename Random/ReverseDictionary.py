d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
new_dict = {k:v for v,k in d.items()}
sum = 0
for i in d.values():
    sum = sum+i
print(sum)
print(new_dict)

l1=['A','C']

filter_dict = {key:d[key] for key in l1}
print(filter_dict)

