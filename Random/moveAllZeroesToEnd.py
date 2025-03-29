
class Solution:
    def pushZeroesToEnd(self,arr):
        zero_Arr=[]
        nonzero_arr=[]
        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         zero_Arr.append(arr[i])
        #     else:
        #         nonzero_arr.append(arr[i])
        arr = [num for num in arr if num != 0] + [num for num in arr if num == 0]
        print(arr)


arr = [1, 2, 0, 4, 3, 0, 5, 0]
# res = ' '.join(map(str,arr[::-1]))
# print(res)
ob = Solution()
ob.pushZeroesToEnd(arr)
