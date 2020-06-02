import unittest
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        res = {}

        # dislikes.sort(key=lambda item:(item[0],item[1]))

        for lst in dislikes:
            a, b = lst[0], lst[1]
            if a not in res:
                res[a] = 0
            if b not in res:
                res[b] = res[a] ^ 1
            else:
                if res[a] ^ 1 != res[b]:
                    print(a, b)
                    return False

        return True


class TestSolution(unittest.TestCase):
    def test_possibleBipartition(self):
        param50, param51 = 5, [[1, 2], [1, 5], [3, 4]]
        param30, param31 = 5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        param20, param21 = 3, [[1, 2], [1, 3], [2, 3]]
        param10, param11 = 4, [[1, 2], [1, 3], [2, 4]]

        solution = Solution()

        self.assertEqual(True, solution.possibleBipartition(param50, param51))
        self.assertEqual(False, solution.possibleBipartition(param30, param31))
        self.assertEqual(False, solution.possibleBipartition(param20, param21))
        self.assertEqual(True, solution.possibleBipartition(param10, param11))


if __name__ == '__main__':
    unittest.main()
