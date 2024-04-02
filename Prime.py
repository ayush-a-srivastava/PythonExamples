def isPrime(n):
     for i in range(2,n):
         if(n%i == 0):
             return False
     return True

num = int(input("Enter any number: "))
res = isPrime(num)
if res == False:
    print("Not a prime number")
else:
    print("Prime Number")



