data = {3: "Apple", 1: "Banana", 4: "Cherry", 2: "Date"}

# sort = dict(sorted(data.items(), key = lambda x: x[0]))

# Another way
sort = dict(sorted(data.items()))
print(sort)