def isPrime(st,end):
    prime = []

    for i in range(st,end+1):
        for j in range(2,i):
          if i%j == 0:
            break
        else:
            prime.append(i)
    print("Prime numbers are: ",prime)

start_Range = int(input("Enter the starting: "))
end_Range = int(input("Enter the ending: "))
isPrime(start_Range,end_Range)