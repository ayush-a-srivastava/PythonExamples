string = input("Enter any string: ")

res = ""
for i in range(1,len(string)+1):
    res = res + string[0:i]
print(res)