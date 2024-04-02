# s = "Kanan is an engineer"
# tar = "an"
# d= {}
#
# for i in s:
#     d[i] = s.count(i)
# print(d)
import re

# Initialising string
s = 'Kanan is an engineer'
res1 = len(re.findall('(?=(an))',s))
s.find("an")
print(res1)
print(s.count('an'))