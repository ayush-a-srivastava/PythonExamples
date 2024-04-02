from functools import reduce

res = lambda x:x+10
print(res(2))

l_cube = lambda x:x*x*x
print(l_cube(4))

sq = [lambda arg =x:arg*10 for x in range(1,5)]
for i in sq:
    print(i())

l = [1,24,6,8,11,13,14]
re = list(filter(lambda x: x%2==0,l))
print(re)

f_l = list(map(lambda x : x*2,l))
print(f_l)

great =  reduce(lambda a,b: a if a>b else b, l)
print(great)