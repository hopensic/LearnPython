from collections import Counter
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = float('-inf')
        for i in range(len(arr) - 1, 0, -1):
            max_value = max(max_value, arr[-1])
            arr[-1] = arr[i - 1]
            arr[i - 1] = max_value
        arr[-1] = -1
        return arr


nums = [17]
solution = Solution()
print(solution.replaceElements(nums))
