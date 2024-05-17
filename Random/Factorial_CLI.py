import sys

if len(sys.argv) != 2:
    print("Usage: python FindMissingNumber.py must expect single argument.")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)

fact = 1
n = num

while n > 1:
    fact = fact * n
    n = n - 1

print(fact)
