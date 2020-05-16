from collections import deque
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        if len(num) == 1:
            return num[0]

        lst = deque()
        lst.append(num[0])
        for i in range(1, len(num)):
            while lst and num[i] < lst[-1] and k > 0:
                lst.pop()
                k -= 1
            if k == 0:
                break
            lst.append(num[i])
        else:
            res = []
            while len(lst) > 0:
                res.append(lst.popleft())
            while k > 0:
                res.pop()
                k -= 1
            s = (''.join(res)).lstrip("0")
            return '0' if len(s) == 0 else s

        s = (''.join(lst) + num[i:]).lstrip('0')
        return '0' if len(s) == 0 else s


class TestSolution(unittest.TestCase):
    def test_removeKdigits(self):
        param90, param91 = "10", 1
        param80, param81 = "1000", 4
        param70, param71 = "1000", 2
        param60, param61 = "12700354", 2
        param50, param51 = "10200", 1
        param40, param41 = "10", 2
        param30, param31 = "54321", 2
        param20, param21 = "12345", 1
        param10, param11 = "37684219", 3

        solution = Solution()

        self.assertEqual('0', solution.removeKdigits(param90, param91))
        self.assertEqual('0', solution.removeKdigits(param80, param81))
        self.assertEqual('0', solution.removeKdigits(param70, param71))
        self.assertEqual('100354', solution.removeKdigits(param60, param61))
        self.assertEqual('200', solution.removeKdigits(param50, param51))
        self.assertEqual('0', solution.removeKdigits(param40, param41))
        self.assertEqual('321', solution.removeKdigits(param30, param31))
        self.assertEqual('1234', solution.removeKdigits(param20, param21))
        self.assertEqual('34219', solution.removeKdigits(param10, param11))


if __name__ == '__main__':
    unittest.main()
