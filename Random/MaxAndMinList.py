from functools import reduce


def max_and_min(arr):
    min_val = arr[0]
    max_val = arr[0]

    for i in arr[1:]:
        if i>max_val:
            max_val=i
        elif i<min_val:
            min_val=i
    print(max_val, min_val)

arr = [11,4,12,150,23,-1,19,2]
max_and_min(arr)

larg = reduce(lambda a,b: a if a>b else b,arr)
small = reduce(lambda a,b: a if a<b else b,arr)
print("The given list is: ",arr)
print("Maximum ele : ",larg)
print("Minimum ele: ",small)

