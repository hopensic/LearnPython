import unittest
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dic = {0: 0}
        res = []
        for i in range(num + 1):
            res.append(dic[i] if i in dic else 1 + dic[i & (i - 1)])
            dic[i] = res[-1]
        return res


class TestSolution(unittest.TestCase):
    def test_countBits(self):
        param50 = 10
        param30 = 4
        param20 = 3
        param10 = 2

        solution = Solution()

        self.assertEqual([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2], solution.countBits(param50))
        self.assertEqual([0, 1, 1, 2, 1], solution.countBits(param30))
        self.assertEqual([0, 1, 1, 2], solution.countBits(param20))
        self.assertEqual([0, 1, 1], solution.countBits(param10))


if __name__ == '__main__':
    unittest.main()
