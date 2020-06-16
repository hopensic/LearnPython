import unittest
from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[n]


class TestSolution(unittest.TestCase):
    def test_checkInclusion(self):
        param80, param81 = [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
        param70, param71 = [2, 1], [1, 2, 1, 3, 3, 2]
        param60, param61 = [1, 3, 2, 4, 2], [3, 1, 4, 2, 4]
        param50, param51 = [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
        param40, param41 = [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]
        param30, param31 = [1, 2, 1, 1], [1, 1, 1]
        param20, param21 = [1, 4, 2], [1, 2, 4]
        param10, param11 = [1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1]

        solution = Solution()

        # a = [1,3,5,6,7,8]
        # b = a[::-1]


        self.assertEqual(2, solution.maxUncrossedLines(param80, param81))
        self.assertEqual(2, solution.maxUncrossedLines(param70, param71))
        self.assertEqual(3, solution.maxUncrossedLines(param60, param61))
        self.assertEqual(2, solution.maxUncrossedLines(param50, param51))
        self.assertEqual(3, solution.maxUncrossedLines(param40, param41))
        self.assertEqual(3, solution.maxUncrossedLines(param30, param31))
        self.assertEqual(2, solution.maxUncrossedLines(param20, param21))
        self.assertEqual(5, solution.maxUncrossedLines(param10, param11))


if __name__ == '__main__':
    unittest.main()
