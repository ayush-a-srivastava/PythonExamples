num = 153
sum = 0
n = num

while(n!=0):
    temp = n % 10
    sum = sum + (temp ** 3)
    n = n//10
if(num == sum):
    print("Armstrong number")
else:
    print("Not Armstrong number")