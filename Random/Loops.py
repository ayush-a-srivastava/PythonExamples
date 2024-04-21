i=1
while i<=10:
    i += 1
    if i==5:
        continue
    print(i)

print("That's over")

names = ["Ayush","AKshat","Vishal"]
actions = ["Codes","Tests","Deploys"]

print("")
for action in actions:
 for name in names:
        print(name + " " + action + ".")
output =[f'{name} {action}' for name,action in zip(names,actions)]
formatted = ", ".join(output)
print(formatted)