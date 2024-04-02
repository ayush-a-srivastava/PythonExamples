def outer_func(x,y):
    def con(x,y):
        return x+y

    z = con(x,y)
    z = z + "developers"
    return z


res = outer_func("Ayush","AKash")
print(res)

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# modify item
list1[1][2][2][1] = 3500
# print final result
print(list1)