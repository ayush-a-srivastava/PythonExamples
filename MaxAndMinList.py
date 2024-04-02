arr = [10,3,19,14,2,13]
print("Maximum is : ",max(arr) , "\nMinimum is: " , min(arr))

def max(arr):
 max = arr[0]
 for i in range(len(arr)):
    if max<arr[i]:
        max = arr[i]
    return max

def min(arr):
 min=arr[0]
 for i in range(len(arr)):
    if min>arr[i]:
        min = arr[i]
    return min
