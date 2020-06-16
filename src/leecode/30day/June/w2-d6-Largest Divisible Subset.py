from collections import defaultdict
from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        le = len(nums)
        if le < 2:
            return nums
        key, maxlen = nums[0], -1
        nums.sort()
        dic = defaultdict(list)
        dic[nums[0]].append(nums[0])

        for i in range(1, le):
            tmp_key, tmp_max = -1, -1
            if nums[i] not in dic:
                dic[nums[i]].append(nums[i])
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(dic[nums[j]]) > tmp_max:
                        tmp_max = len(dic[nums[j]])
                        tmp_key = nums[j]
            if tmp_max > 0:
                dic[nums[i]].extend(dic[tmp_key])
            if len(dic[nums[i]]) > maxlen:
                maxlen = len(dic[nums[i]])
                key = nums[i]

        return dic[key]


nums = [2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24]
# nums = [2, 3, 8, 9, 27]
# nums = [1,2,4,8]
# nums = [4, 8, 10, 240]
# nums = [546, 669]
s1 = Solution()
print(s1.largestDivisibleSubset(nums))
