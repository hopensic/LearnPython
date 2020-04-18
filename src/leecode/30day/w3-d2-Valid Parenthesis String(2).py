import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for ch in s:
            if ch == "(":
                cmax += 1
                cmin += 1
            elif ch == ")":
                cmax -= 1
                cmin = max(cmin - 1, 0)
            else:
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


class TestSolution(unittest.TestCase):
    def test_method(self):
        param0 = "(*"
        param1 = "(())(())(((()*()()()))()((()()(*()())))(((*)()"
        param2 = "()"
        param3 = "(*)"
        param4 = "(*()"
        param5 = "(*))"
        solution = Solution()
        self.assertEqual(True, solution.checkValidString(param0))
        self.assertEqual(False, solution.checkValidString(param1))
        self.assertEqual(True, solution.checkValidString(param2))
        self.assertEqual(True, solution.checkValidString(param3))
        self.assertEqual(True, solution.checkValidString(param4))
        self.assertEqual(True, solution.checkValidString(param5))


if __name__ == '__main__':
    unittest.main()
