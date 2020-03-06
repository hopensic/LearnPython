from datetime import datetime

'''
tag: ^1365 ^easy ^array ^hash-table
name: ^(How Many Numbers Are Smaller Than the Current Number)
'''


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        le = len(nums)
        lst = [0] * le
        for i in range(le - 1):
            for j in range(i + 1, le):
                if nums[i] > nums[j]:
                    lst[i] += 1
                elif nums[j] > nums[i]:
                    lst[j] += 1

        return lst


nums = [7, 7, 7, 7]

t1 = datetime.now()
s = Solution()
print(s.smallerNumbersThanCurrent(nums))
t2 = datetime.now()
print(t2 - t1)
