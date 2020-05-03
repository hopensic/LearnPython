from collections import Counter
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        last_num = float('-inf')

        for i in range(len(A)):
            if A[i] <= last_num:
                max_value = last_num
                last_num = A[i]
                break
            last_num = A[i]
        else:
            return False
        if i == 1:
            return False
        last_num = max_value
        for k in range(i, len(A)):
            if A[k] >= last_num:
                break
            last_num = A[k]
        else:
            return True
        return False


nums = [3,5,5]
solution = Solution()
print(solution.validMountainArray(nums))
