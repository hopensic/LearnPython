from collections import Counter
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i] ** 2
        A.sort()


nums = [-4, -1, 0, 3, 10]
solution = Solution()
print(solution.sortedSquares(nums))
