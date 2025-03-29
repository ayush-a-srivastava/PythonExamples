s = "Malayalam"

s1 = s[::-1]
if(s==s1):
    print("Palindrome")
else:
    print("Not Palindrome")

#############################################
rev=""
for i in range(len(s)-1,-1,-1):
    rev = rev+s[i]
# print(rev)
if(rev==s):
    print("Palindrome")
else:
    print("Not Palindrome")