l = ['1', 7,2, 4, 1, '3',"hi", '2', '5', "hello",5,6,7,7]

# Dictionary to store occurrences
occurrences = {}

for item in l:
    normalized_item = str(item)  # Normalize to string
    if normalized_item in occurrences:
        occurrences[normalized_item] += 1
    else:
        occurrences[normalized_item] = 1

# Display the results
for key, count in occurrences.items():
    print(f"Element {key} occurs {count} time(s)")
