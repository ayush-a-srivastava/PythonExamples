class Dict2Class(object):
    def __init__(self,mydict):
        for k in mydict:
           setattr(self,k,mydict[k])

my_dict = {"Name":"Ayush","Age":26,"Location":"Noida"}
di= Dict2Class(my_dict)
print(di.Name, di.Age, di.Location)
print(type(di))
