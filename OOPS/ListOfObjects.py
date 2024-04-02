class Lobj:

    def __init__(self,name,age):
        self.name = name
        self.age = age

l=[]

l.append(Lobj("ayush",25))
l.append(Lobj("akash",27))
l.append(Lobj("akshay",24))

for i in l:
    print(i.name, i.age)

# Accessing the elements individually
print(l[0].name)
print(l[1].age)