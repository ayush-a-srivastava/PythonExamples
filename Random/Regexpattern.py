from Lambda import re


def match_text(s):
    pattern='ab{4,8}'
    if(re.search(pattern,s)):
        return "match found"
    else:
        return "match not found"




print(match_text("aaaabbbbc"))