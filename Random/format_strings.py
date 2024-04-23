name = "Ayush"
age = 26

print(name + "'s" + " age is: ",age)

# %s formatting
message = "%s's age is: %s" %(name,age)
print(message)

# Using string.format()
message = "{}'s age is: {}".format(name,age)
print(message)
message = "{name}'s age is: {age}".format(name=name,age=age)
print(message)

# Dictionary

info = {"name":"Ayush","age":26}
message = "{name}'s age is: {age}".format(**info)
print(message)

# Using f'string
message = f"{name}'s age is: {age}"
print(message)
message = f"{info['name']}'s age is: {age}"
print(message)

# Loop
num = 2
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")