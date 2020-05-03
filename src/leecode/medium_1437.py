from datetime import datetime
from typing import List

'''
tag: ^1437 ^medium ^array
name: ^(Check If All 1's Are at Least Length K Places Away)
'''


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums)==1:
            return True

        min_value = 10001
        distance = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                break
        else:
            return True

        for j in nums[i+1:]:
            if j == 1:
                min_value = min(min_value, distance)
                distance = 0
            else:
                distance += 1

        return min_value >= k


nums = [0,0,0]
k = 1

t1 = datetime.now()
s = Solution()
print(s.kLengthApart(nums, k))
t2 = datetime.now()
print(t2 - t1)
