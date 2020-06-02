import unittest
from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        set1, set2 = set(), set()
        idx1, idx2 = 0, 0
        res = 0

        #  t 传1或者2 ，1,代表只对idx1++，2代表只对idx2++
        def check(s1: set, s2: set, t: int):
            nonlocal res, idx1, idx2
            if len(s1 & s2) > 0:
                res += 1
                s1.clear()
                s2.clear()
                if t == 1:
                    idx1 += 1
                elif t == 2:
                    idx2 += 1
                return True
            return False

        while idx1 < len(A) and idx2 < len(B):
            set1.add(A[idx1])
            if check(set1, set2, 1):
                continue
            else:
                idx1 += 1
            set2.add(B[idx2])
            if check(set1, set2, 2):
                continue
            else:
                idx2 += 1
        while idx1 < len(A):
            set1.add(A[idx1])
            idx1 += 1
        while idx2 < len(B):
            set2.add(B[idx2])
            idx2 += 1
        if len(set1 & set2) > 0:
            res += 1

        return res


class TestSolution(unittest.TestCase):
    def test_checkInclusion(self):
        param70, param71 = [2, 1], [1, 2, 1, 3, 3, 2]
        param60, param61 = [1, 3, 2, 4, 2], [3, 1, 4, 2, 4]
        param50, param51 = [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]
        param40, param41 = [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]
        param30, param31 = [1, 2, 1, 1], [1, 1, 1]
        param20, param21 = [1, 4, 2], [1, 2, 4]
        param10, param11 = [1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1]

        solution = Solution()

        self.assertEqual(2, solution.maxUncrossedLines(param70, param71))
        self.assertEqual(3, solution.maxUncrossedLines(param60, param61))
        self.assertEqual(2, solution.maxUncrossedLines(param50, param51))
        self.assertEqual(3, solution.maxUncrossedLines(param40, param41))
        self.assertEqual(3, solution.maxUncrossedLines(param30, param31))
        self.assertEqual(2, solution.maxUncrossedLines(param20, param21))
        self.assertEqual(5, solution.maxUncrossedLines(param10, param11))


if __name__ == '__main__':
    unittest.main()
