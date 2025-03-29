import sys

n = int(input("Enter number: "))
fact = 1
try:
    while(n>0):
        fact = fact*n
        n = n-1
    print("Factorial is: ", fact)
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)
