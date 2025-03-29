'''
In python, doesn't allow Method overloading just like traditional ways in Java and C++.
But still we can achieve using default arguments, using *args/*kwargs and @singledispatch
'''

from functools import singledispatch

@singledispatch
def display(value):
    print("Default value:",value)


@display.register(int)
def _(value):
    print("Integer: ", value)

@display.register(str)
def _(value):
    print("String: ", value)

@display.register(list)
def _(value):
    print("List: ", value)

display([1,2,3])
display(10)
display("Ayush")
display(12.4)