import random

def generate_password(length):
    password = ''.join(random.choices(all_characters, k=length))
    return password

Upper_char_list = [] # 65 - 90
digit_list = []    # 48 - 57
symbols_list = []  # 32-47
lower_char_list = []  # 97-122

for upper in range(65,91):
    Upper_char_list.append(chr(upper))

for digit in range(48,58):
    digit_list.append(chr(digit))

for symbol in range(32,48):
    symbols_list.append(chr(symbol))

for lower in range(97,123):
    lower_char_list.append(chr(lower))

all_characters = Upper_char_list + lower_char_list + digit_list + symbols_list
length = int(input("Enter the password length : "))
password = generate_password(length)
print("Generated Password : ", password)

