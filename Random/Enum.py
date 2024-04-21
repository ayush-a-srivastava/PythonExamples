'''
Enum are set of symbolic names that are bound to unique values.
They are most useful when you want to create a set of name constants ro you have fixed set of values you
want to work with.
'''

from enum import Enum

class Weekday(Enum):

    MONDAY=1
    TUESDAY=2
    WEDNESDAY=3
    THURSDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7
print(Weekday.MONDAY)
print(Weekday(4))
print(Weekday.MONDAY.value)
print(type(Weekday.MONDAY))
print(Weekday.MONDAY.name)