from datetime import datetime

'''
tag: ^1389 ^easy ^array
name: ^(Create Target Array in the Given Order)
'''


class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        res = []
        for idx,i in enumerate(index):
            res.insert(i, nums[idx])
        return res


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

t1 = datetime.now()
s = Solution()
print(s.createTargetArray(nums, index))
t2 = datetime.now()
print(t2 - t1)
