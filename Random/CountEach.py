s1 = ["a", "a", "a", "b", "c", "c", "d"]

d = {}
for i in s1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
# return the element with maximum frequency
max_frequency = 0
max_ele = None
for key in d:
    if d[key] > max_frequency:
        max_frequency = d[key]
        max_ele = key
print(f"The element with maximum frequency: {max_ele} and the frequency : {max_frequency}")


