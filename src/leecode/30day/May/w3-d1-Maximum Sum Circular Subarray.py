from collections import deque
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mn = float('inf')
        le = len(A)
        if le == 1:
            return A[0]
        mx = A[0]
        local, gbl, prefix_sum = [A[0]], [A[0]], [A[0]]
        for i in range(1, le):
            prefix_sum.append(A[i] + prefix_sum[i - 1])
            local.append(max(A[i], A[i] + local[i - 1]))
            mx = max(mx, local[-1])
            gbl.append(mx)
            for j in range(i):
                mn = min(mn, prefix_sum[i] - prefix_sum[j])

        # s1, s2 = A[-1], A[0]
        #
        # for i in range(le - 1):
        #     s1 = A[-1] + prefix_sum[i]
        #     s2 += prefix_sum[le - i - 1] - prefix_sum[le - i - 2]
        #     mx = max(mx, s1, s2)

        return max(mx, prefix_sum[le - 1] - mn)


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
