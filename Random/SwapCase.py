s = "abCd eF"
# s1 = ""
# for i in range(len(s)):
#     if s[i] == s[i].lower():
#         s1 = s[i].upper()
#     else:
#         s1 = s[i].lower()
#     print(s1 , end = "")
res = [char.upper() if char.islower() else char.lower() for char in s]
print(''.join(res))