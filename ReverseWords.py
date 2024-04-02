s = "Hello ayush how are you"
s1 = s.split()[::-1]
print(s1)
l = []

for i in s1:
    l.append(i)
print(" ".join(l))
