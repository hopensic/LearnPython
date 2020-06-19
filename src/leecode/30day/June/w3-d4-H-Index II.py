import unittest
from typing import List
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        le = len(citations)
        left = 0
        right = le - 1
        while True:
            if left == right:
                return left + 1
            mid = int((left + right) / 2)
            if mid == 0:
                return citations[mid]
            # if citations[mid] >= mid + 1 >= citations[mid - 1]:
            #     return mid + 1
            h = citations[mid]
            if citations[-h] < h:  # 应该从-h的index值向右移
                if le - h >= mid:  # -h的index值大于mid
                    left = mid + 1
                else:
                    left = le - h
                    right = mid
                continue
            if citations[-h - 1] > h:  # 应该从-h的index值向左移
                if le - h - 1 >= mid:  # -h-1的index值大于mid
                    left = mid
                    right = le - h - 1
                else:
                    right = mid - 1
                continue
            return h


class TestSolution(unittest.TestCase):
    def test_hIndex(self):
        param7 = [1, 3, 3, 4, 6, 6, 7, 8, 10, 12]
        param6 = [1, 3, 3, 4, 6, 6, 7, 8, 10]
        param5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        param4 = [1, 3, 3, 6, 6, 6, 7, 8, 10]
        param3 = [1, 1, 1, 2, 3, 4, 5]
        param2 = [0, 1, 3, 5, 6]
        param1 = [1, 1, 1, 2, 2, 3, 4, 5]

        solution = Solution()
        # self.assertEqual(6, solution.hIndex(param7))
        # self.assertEqual(5, solution.hIndex(param6))
        # self.assertEqual(5, solution.hIndex(param5))
        # self.assertEqual(6, solution.hIndex(param4))
        # self.assertEqual(3, solution.hIndex(param3))
        # self.assertEqual(3, solution.hIndex(param2))
        self.assertEqual(3, solution.hIndex(param1))


if __name__ == '__main__':
    unittest.main()
