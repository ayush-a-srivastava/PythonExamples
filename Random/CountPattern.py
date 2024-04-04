def find_occur(s,substr):
    occurence = []
    length = len(substr)
    for i in range(len(s) - length + 1):
        if s[i:i+length] == substr:
            occurence.append(i)
    return occurence


s = 'CCDDCCCCDDCC'
substr = "CC"
print("Indexes are: ",find_occur(s,substr))
print("Total count are: ", len(find_occur(s,substr)))