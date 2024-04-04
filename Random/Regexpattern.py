import re

def match_text(s):
    pattern='ab{3,8}'
    if(re.search(pattern,s)):
        return "match found"
    else:
        return "match not found"

print(match_text("aaaabbbbc"))
print(re.match("bb","aaaabbbbc")) #Only return if match is found at the beginning of string
print(re.findall("bb","aaaabbbbc"))  # returns a list of all matches within the string
print(re.search("bb","aaaabbbbc"))   # return the first match from anywhere in the string