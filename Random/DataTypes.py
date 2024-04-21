b = False
print(type(b))

comp = 5+6j
print(comp.real)
print(comp.imag)

#Built-in methods
gpa = 3.45
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))

import math
print(math.pi)
print(math.sqrt(100))
print(math.ceil(gpa))
print(math.floor(gpa))

users = ["ayush","akshat","ajay"]
users.extend(["manish","akash"])
print(users)
users.insert(2,"Ankit")
print(users)
users[1:3] = ["Mohan","Sunny"]
print(users)

# it removes the exact name
users.remove("Sunny")
print(users)
# if not given it will delete from the last
print(users.pop())
print(users)
# it will delete using index
del users[1]
print(users)
users[2:4] = ['Manohar',"Laxmi"]
print(users)
users.sort(key=str.lower)
print(users)

nums=[5,4,25,1,3]
# It will simply sorted the list without modifying the actual list
print(sorted(nums,reverse=True))
print(nums)

# Ways to copy a list but they won't modify the actual list
mycopy = nums.copy()
mynums = nums[:]
mynumscopy = list(nums)
print(mycopy)
print(mynums)
mynumscopy.sort()
print(mynumscopy)
print(nums)

tup = (1,3,4,5,3,3,3)
anothertuple = (2,3,4)
print(tup)
print(anothertuple)
(*one, two) = anothertuple
print(one)
print(two)
print(tup.count(3))
print(tup.index(3))


dic = {1:'A',2:'B'}
dic1 = dic
print(dic)
print(dic1)
print(isinstance(dic1,dict))
print(dic[1])
print(dic.get(2))

#Change values
dic[1] = "C"
dic.update({3:"D"})
print(dic)

# Remove item
dic.pop(2)
print(dic)

dic[4] = "E"
print(dic)

# popitem will delete from the last and will return tuple
print(dic.popitem())
print(dic)

dic[4] = "E"
del dic[4]
print(dic)

#Copy dictionary
print("")
# This will not create a copy but will create a reference both pointing to the same dictionary
# If any changes made to dictionary 1 it will also reflect to dictionary 2 which we don't want.
# d1 = dic
# print(d1)
# print(dic)
# print(Bad Copy")
# d1[7] = "G"
# print(dic)

d1 = dic.copy()
d1[6] = "F"
print("Good Copy")
print(d1)
print(dic)

# Nested Dictionaries

member1 = {"name":"Ayush","age":26}
member2 = {"City":"Bangalore","domain":"testing"}
member3 = {"k1":member1,"k2":member2}
print(member3)
print(member3["k1"]['age'])

# Sets
print("")
s = {1,2,2,3,4,3}
s1 = set((1,2,2,3,3,4,4,6,7,8))
print(s)
print(s1)
new_s = {2,3,True,1,0,False}
print(new_s)

#Add to set
s.add(8)
print(s)
s.update(s1)
print(s)

# Merge two sets
one = {1,2,3}
two = {4,5,6}
mergeset = one.union(two)
print(mergeset)

# Keep only the duplicates
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# Keep all except the duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)