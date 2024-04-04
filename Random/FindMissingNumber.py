
# Example 1

def find_missing(l):
    if not l:
        print("Empty")

    minimum = min(l)
    maximum = max(l)

    num_set = set(l)
    new_l = []
    for i in range(minimum,maximum+1):
        if i not in num_set:
            new_l.append(i)
    print("Missing numbers are: ", new_l)

l = [4,12,10,11,2]
find_missing(l)
#-------------------------------------------------------------------------------------------

# Example 2
def missing(li):
    mini = min(li)
    maxi = max(li)

    set_list = set(li)
    new_l = []
    for i in range(mini,maxi+1):
        if i not in set_list:
            new_l.append(i)
    print("Missing numbers: ", new_l)

li = [3,12,5,6,9]
missing(li)











