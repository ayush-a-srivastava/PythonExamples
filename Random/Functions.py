def add(num1=0,num2=0):
    if (type(num1) is not int or type(num1) is not int):
        return
    return num1 + num2

total = add(4,5)
print(total)

def multi_args(*args):
    print(args)
    print(type(args))

multi_args("Ayush","AKshat","Manish")

def key_multi_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

key_multi_args(name="ayush",age=26)
