'''

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15[
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
'''

print("Thank you for choosing Python Pizza Deliveries!")
size = input("Enter the pizza size: ")
add_pepperoni = input("Do you want pepperoni?: ")
extra_cheese = input("Do you want extra cheese?: ")
bill = 0
if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your final bill is: ${bill}.")
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your final bill is: ${bill}.")
elif size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your final bill is: ${bill}.")
