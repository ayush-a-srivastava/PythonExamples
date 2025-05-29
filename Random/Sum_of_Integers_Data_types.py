l = [
    [2,4,11,5],
    "Suraj",
    34.2,
    "Akash",
    23.7,
    (6,2,12,21),
    [7,3,5,1],
    23,
    True,
    56,
    {'a': 1, 'b': 2, 'c': 3},
    False,
    {'x': 4, 'y': 5, 'z': 6}
]


total = 0

for item in l:
    if isinstance(item, (int, float)):
        total+= item
    elif isinstance(item, (list, tuple)):
        for i in item:
            if isinstance(i, (int, float)):
                total+= i
    elif isinstance(item, dict):
        for value in item.values():
            if isinstance(value, (int, float)):
                total+= value
print("Total sum: ", total)
