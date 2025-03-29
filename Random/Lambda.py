'''
Map(): Used map when you have to perform a function to each element in an iterable[list,tuple] and
        produce a new iterable
filter(): Use filter when you have to selectively include elements based on a condition.
reduce(): Use reduce when you have to do cumulative functions(add,products) and import from functools
'''

from functools import reduce

# res = lambda x:x+10
# print(res(2))
#
# l_cube = lambda x:x*x*x
# print(l_cube(4))

# sq = [lambda x =x:x*10 for x in range(1,5)]
# for i in sq:
#     print(i())
#
l = [1,24,6,8,11,13,14]
# re = list(filter(lambda x: x%2==0,l))
# print(re)
#
f_l = list(map(lambda x : x*2,l))
print(f_l)

l1 = [11,12,1,2,4,32,21,20]
max =  reduce(lambda a,b: a if a>b else b, l1)
min =  reduce(lambda a,b: a if a<b else b, l1)
print("Maximum: ",max)
print("Minimum: ",min)

# result = filter(lambda x:x%2==0,range(1,101))
# for i in result:
#     print(i,end = " ")

# Creating a dictionary
data = {3: "Apple", 1: "Banana", 4: "Cherry", 2: "Date"}
sorted_dict = dict(sorted(data.items()))
print(sorted_dict)

# Creating a dictionary
data = {3: "Apple", 1: "Banana", 4: "Cherry", 2: "Date"}

# Sorting based on values
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

# Printing the sorted dictionary
print(sorted_dict)
