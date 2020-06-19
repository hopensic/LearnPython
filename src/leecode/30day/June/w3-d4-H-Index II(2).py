import unittest
from typing import List
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


# TODO ^ongoing ^binary-search


class Solution:

    def hIndex2(self, citations: List[int]) -> int:
        le = len(citations)
        left = 0
        right = le - 1
        while left <= right:
            # mid代表了元素的index，表示它左边有几个元素
            mid = (left + right) // 2
            if citations[mid] == le - mid:
                return le - mid
            elif citations[mid] > le - mid:
                right = mid - 1
            else:
                left = mid + 1
        return le - left


class TestSolution(unittest.TestCase):
    def test_hIndex2(self):
        param8 = [1, 3, 5, 7, 9]
        param7 = [1, 3, 3, 4, 6, 6, 7, 8, 10, 12]
        param6 = [1, 3, 3, 4, 6, 6, 7, 8, 10]
        param5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        param4 = [1, 3, 3, 6, 6, 6, 7, 8, 10]
        param3 = [1, 1, 1, 2, 3, 4, 5]
        param2 = [0, 1, 4, 5, 6]
        param1 = [1, 1, 1, 2, 2, 3, 4, 5]

        solution = Solution()
        self.assertEqual(3, solution.hIndex2(param8))
        self.assertEqual(6, solution.hIndex2(param7))
        self.assertEqual(5, solution.hIndex2(param6))
        self.assertEqual(5, solution.hIndex2(param5))
        self.assertEqual(6, solution.hIndex2(param4))
        self.assertEqual(3, solution.hIndex2(param3))
        self.assertEqual(3, solution.hIndex2(param2))
        self.assertEqual(3, solution.hIndex2(param1))


if __name__ == '__main__':
    unittest.main()
