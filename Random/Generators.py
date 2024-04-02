'''
Generators are the function when you call this function it will give the items one by one
untill you ask for the next one.
'''

def count_to_ten():
    n=1
    while(n<=10):
        yield n
        n+=1

counter = count_to_ten()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


