from collections import Counter
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] *= -1
        res = []
        for idx, i in enumerate(nums):
            if i > 0:
                res.append(idx + 1)
        return res


# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [2, 3, 3, 1, 6, 8, 6, 1]
solution = Solution()
print(solution.findDisappearedNumbers(nums))
