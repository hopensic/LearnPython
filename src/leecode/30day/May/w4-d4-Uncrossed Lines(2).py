import unittest
from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        le1, le2 = len(A), len(B)
        dp = [[0] * le2 for _ in range(le1)]
        dp[-1][-1] = 1 if A[-1] == B[-1] else 0

        for i in range(le2 - 2, -1, -1):
            dp[-1][i] = max(dp[-1][i + 1], 1 if A[-1] == B[i] else 0)
        for i in range(le1 - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1], 1 if A[i] == B[-1] else 0)

        for i in range(le1 - 2, -1, -1):
            for j in range(le2 - 2, -1, -1):
                dp[i][j] = max(dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0, dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]


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
