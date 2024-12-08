inp = int(input("How many elements you want to add: "))
ele = []
print("Enter the elements: ")
for i in range(inp):
    n = int(input())
    ele.append(n)
total_rotation = int(input("Enter the steps you want to do left rotation: "))
ele = ele[total_rotation:] + ele[:total_rotation]
print(ele)
