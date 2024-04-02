d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
new_dict = {v:k for k,v in d.items()}
print(new_dict)

l1=['A','C']

filter_dict = {key:d[key] for key in l1}
print(filter_dict)
