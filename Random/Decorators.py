'''
Decorators are a way to modify the behaviour of functions and methods without changing the actual code.
They allow you to add functionality to an existing definition dynamically
'''

# def say_hi(func):
#     def wrapper():
#         print("First say Hi")
#         func()
#     return wrapper
#
# @say_hi
# def hello():
#     print("Hello Ayush")

# hello()

def print_add(func):
    def wrapper(*ar):
        print("Total sum: ")
        res = func(*ar)
        return res
    return wrapper

@print_add
def add(a,b,c,d):
    return a+b+c+d

print(add(2,3,4,5))


def say(func):
    def wrapper():
        print("Before printing")
        func()
        print("After printing")
    return wrapper

@say
def hello():
    print("Hello")

hello()