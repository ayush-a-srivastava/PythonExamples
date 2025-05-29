integer = int(input("Enter any number: "))

print("Before Reversing: ", integer)
reverse_no = 0
while integer > 0:
    last_digit = integer % 10
    reverse_no = (reverse_no * 10) + last_digit
    integer = integer // 10

print("After reversing: ", reverse_no)