import copy

'''
copy.deepcopy()
	- Creates the completely independent copy, including all nested objects.
	- Changes in the list does not reflect in the original.

'''
# l = [1,23,21,19,45,67]
l = [[1,2,5],[4,5,6]]
deep_l = copy.deepcopy(l)

deep_l[1][0] = 20
print("Deepcopied list: ", deep_l)
print("Original list : ", l)


'''
copy.copy() or Shallow copy
	- If the original object contains mutable elements(list/dictionaries), it will reflect in the copied object as well.

'''
new_l = [[1,2,5],[4,5,6]]
copy_l = copy.copy(new_l)
copy_l[0][1] = 18
print("Shallow copied list: ", copy_l)
print("Original list : ", new_l)