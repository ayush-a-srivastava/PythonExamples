'''
This program tells us how many weeks we have left if we live untll 90.
'''

MAX_AGE = 90
WEEKS = 52

age = int(input("Enter your age: "))
remaining_age = MAX_AGE - age
weeks_left = remaining_age * WEEKS
print(f"You have {weeks_left} weeks left.")