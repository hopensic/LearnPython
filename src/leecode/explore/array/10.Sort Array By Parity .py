from collections import Counter
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i <= j:
            while i <= j and A[i] % 2 == 0: i += 1
            while i <= j and A[j] % 2 == 1: j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A


nums = [3,1,1,3,4,5,4,6,7]
solution = Solution()
print(solution.sortArrayByParity(nums))
