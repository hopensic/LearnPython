from collections import Counter
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        compared = heights[:]
        compared.sort()
        return len(heights) - [compared[i] - heights[i] for i in range(len(heights))].count(0)


nums = [1]
solution = Solution()
print(solution.heightChecker(nums))
