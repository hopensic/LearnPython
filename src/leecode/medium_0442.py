from datetime import datetime
from typing import List

'''
tag: ^0442 ^medium ^array ^hash-table
name: ^(Find All Duplicates in an Array)
'''


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        le = len(nums)
        for i in range(le):
            if i == nums[i] - 1:
                continue
            else:
                t = nums[i]
                nums[i] = -1
                while t != nums[t - 1]:
                    k = nums[t - 1]

                    if nums[t - 1] < 0:
                        nums[t - 1] = t
                        break
                    else:
                        nums[t - 1] = t
                        t = k
                else:
                    res.append(t)

        return res


arr1 = [1, 1, 2, 2]
# arr1 = [4, 3, 2, 7, 8, 2, 3, 1]

t1 = datetime.now()
s = Solution()
print(s.findDuplicates(arr1))
t2 = datetime.now()
print(t2 - t1)
