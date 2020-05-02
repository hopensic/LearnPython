from datetime import datetime

import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = 0
        # '*'用于替换成右括号，每遇到n==0，需要清空
        replace_right_star = 0
        # '*'用于替换成左括号，不需要清空
        replace_left_star = 0

        for ch in s:
            if ch == '(':
                if n > 0:
                    replace_right_star = 0
                n += 1
            elif ch == ')':
                n -= 1
                while n < 0:
                    if replace_left_star > 0:
                        replace_left_star -= 1
                        n += 1
                    else:
                        break
                if n < 0:
                    return False
            else:
                replace_right_star += 1
            if n == 0:
                replace_left_star += replace_right_star
                replace_right_star = 0
        if n == 0:
            return True
        # 需要将'*'替换成右括号
        elif n > 0:
            if replace_right_star >= n:
                return True
            else:
                return False
        # 需要将'*'替换成左括号
        else:
            if replace_left_star >= n:
                return True
            else:
                return False


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
