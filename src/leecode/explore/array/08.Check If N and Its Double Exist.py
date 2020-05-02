from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = Counter(arr)
        if c[0] > 1:
            return True
        del c[0]
        le = len([2 * k for k in arr if 2 * k in c])
        return True if le > 0 else False


nums = [10, 2, 5, 3]
solution = Solution()
print(solution.checkIfExist(nums))
