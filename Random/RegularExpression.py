import re

print(re.search(r"9+", "289908"))
print(re.search(r"\d{3}", "hello1234"))


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{3}$'
    return re.match(pattern,email) is not None


pattern1 = "ayush.a.srivastava@gmail.com"
pattern2 = "invalid.com"

print("Email is: ",validate_email(pattern1))
print("Email is: ",validate_email(pattern2))
#-------------------------------------------------------------------------------
def validate_url(url):
    url_pattern = r'^[https://]+[www\.]+[a-zA-Z0-9_-]+\.[a-zA-Z]{3}$'
    return re.match(url_pattern,url) is not None

pattern = "https://www.google.com"
print("URL is: ",validate_url(pattern))

#----------------------------------------------------------------------------
def validate_ip(ip):
    ip_pattern = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(ip_pattern,ip) is not None

pattern = "19.12.45.245"
print("IP is: ",validate_ip(pattern))
# ------------------------------------------------------------------------------
s = "hey ayush how are you"
pattern = r'[\s+]'
res = s.split(pattern)
print(res)

# -----------------------------------------------------------------------
s1 = "filename.txt containes .txt many times .txt manhy many"
pat = r'many'
print(re.search(pat,s1))
print(re.findall(pat,s1), len(re.findall(pat,s1)))