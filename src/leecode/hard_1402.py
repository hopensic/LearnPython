import unittest
import bisect
from datetime import datetime

'''
tag: ^1402 ^hard ^dp
name: ^(Reducing Dishes)
'''


class Solution:
    def maxSatisfaction(self, satisfaction: list) -> int:
        def get_sum(lst):
            t = 0
            for idx, i in enumerate(lst):
                t += (idx + 1) * i
            return t

        res = 0  # 返回值
        le = len(satisfaction)
        satisfaction.sort()
        # 找到>=0的数的最小的索引
        idx = bisect.bisect_left(satisfaction, 0)
        # 如果全是负数 返回0
        if idx == le:
            return 0
        negative_lst, positive_lst = satisfaction[:idx], satisfaction[idx:]
        len_positive, len_negative = len(positive_lst), len(negative_lst)

        # 正数的和
        res = get_sum(positive_lst)
        # 如果没有负数，直接返回正数的和
        if len_negative == 0:
            return res

        # for i in range(1,len_negative+1):

        for idx, i in enumerate(negative_lst[::-1]):
            positive_lst.insert(0, i)
            res = max(res, get_sum(positive_lst))

        return res


class TestSolution(unittest.TestCase):
    def test_maxSatisfaction(self):
        param10 = [-1, -8, 0, 5, -9]
        param9 = [4, 3, 2]
        param8 = [-1,-4,-5]
        param7 =  [-2,5,-1,0,3,-3]

        solution = Solution()
        self.assertEqual(14, solution.maxSatisfaction(param10))
        self.assertEqual(20, solution.maxSatisfaction(param9))
        self.assertEqual(0, solution.maxSatisfaction(param8))
        self.assertEqual(35, solution.maxSatisfaction(param7))


if __name__ == '__main__':
    unittest.main()
