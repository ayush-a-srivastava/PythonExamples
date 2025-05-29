l = [2,12,3,45,1,14,11,20,17,16,5]
print("Before Sorting : ", l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print("After Sorting : ", l)

new_l = [num for num in l if num%2 == 0] + [num for num in l if num%2 != 0]
print("Even + Odd list: ", new_l)