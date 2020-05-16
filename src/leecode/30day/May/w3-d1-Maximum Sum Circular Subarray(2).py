from collections import deque
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        le = len(A)
        mx, mn = A[0], A[0]
        local_max, gbl_max, = [A[0]], [A[0]]
        local_min, gbl_min, = [A[0]], [A[0]]
        total = A[0]
        for i in range(1, le):
            local_max.append(max(A[i], A[i] + local_max[i - 1]))
            mx = max(mx, local_max[-1])
            gbl_max.append(mx)

            local_min.append(min(A[i], A[i] + local_min[i - 1]))
            mn = min(mn, local_min[-1])
            gbl_min.append(mn)
            total += A[i]

        return max(gbl_max[-1], total - gbl_min[-1]) if gbl_max[-1] > 0 else gbl_max[-1]


class TestSolution(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        param90 = [-2, 4, -5, 4, -5, 9, 4]
        param80 = [2, 3]
        param70 = [-2, 3]
        param60 = [2, -3]
        param50 = [-2, -3, -1]
        param40 = [3, -2, 2, -3]
        param30 = [3, -1, 2, -1]
        param20 = [5, -3, 5]
        param10 = [1, -2, 3, -2]

        solution = Solution()

        self.assertEqual(1, solution.maxSubarraySumCircular(param91))
        self.assertEqual(15, solution.maxSubarraySumCircular(param90))
        self.assertEqual(5, solution.maxSubarraySumCircular(param80))
        self.assertEqual(3, solution.maxSubarraySumCircular(param70))
        self.assertEqual(2, solution.maxSubarraySumCircular(param60))
        self.assertEqual(-1, solution.maxSubarraySumCircular(param50))
        self.assertEqual(3, solution.maxSubarraySumCircular(param40))
        self.assertEqual(4, solution.maxSubarraySumCircular(param30))
        self.assertEqual(10, solution.maxSubarraySumCircular(param20))
        self.assertEqual(3, solution.maxSubarraySumCircular(param10))


if __name__ == '__main__':
    unittest.main()
