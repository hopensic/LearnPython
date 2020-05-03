from collections import Counter
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr


nums = [17, 18, 5, 4, 6, 1]
solution = Solution()
print(solution.replaceElements(nums))
