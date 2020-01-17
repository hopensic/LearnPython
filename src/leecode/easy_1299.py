from datetime import datetime

'''
tag: ^1299 ^easy ^array
name: ^(Replace Elements with Greatest Element on Right Side)
'''


class Solution:
    def replaceElements(self, arr):
        le = len(arr)
        if le == 1:
            return [-1]
        elif le == 2:
            arr[-2] = arr[-1]
            arr[-1] = -1
        else:
            big = arr[-1]
            pre = arr[-2]
            for i in range(le - 2, 0, -1):
                if pre >= big:
                    big = pre
                    pre = arr[i - 1]
                    arr[i - 1] = big
                else:
                    pre = arr[i - 1]
                    arr[i - 1] = big
            arr[-2] = arr[-1]
            arr[-1] = -1
            return arr


arr1 = [17, 18, 5, 4, 6, 1]

t1 = datetime.now()
s = Solution()
print(s.replaceElements(arr1))
t2 = datetime.now()
print(t2 - t1)
