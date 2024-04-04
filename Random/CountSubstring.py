s = "Hello Ayush How are Ayush Ayush"
sub = "Ayush"
count = 0
s1 = s.split()
for i in s1:
    if i == sub:
        count+=1
print("The count is: ", count)