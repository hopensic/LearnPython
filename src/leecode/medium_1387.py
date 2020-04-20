import unittest
from datetime import datetime

'''
tag: ^1387 ^medium ^sort ^graph
name: ^(Sort Integers by The Power Value)
'''


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {2 ** i: i for i in range(1, 21)}
        ret_dic = {}
        vdic = {}
        for i in range(lo, hi + 1):
            d = i
            tmp_dic = {d: 0}
            while True:
                if d in dic:
                    for key, value in tmp_dic.items():
                        tmp_dic[key] = value + dic[d]
                    vdic.update(tmp_dic)
                    ret_dic[i] = vdic[i]
                    tmp_dic.clear()
                    break
                elif d in vdic:
                    for key, value in tmp_dic.items():
                        tmp_dic[key] = value + vdic[d]
                    vdic.update(tmp_dic)
                    ret_dic[i] = vdic[i]
                    tmp_dic.clear()
                    break
                if d % 2 == 0:
                    d = int(d / 2)
                else:
                    d = 3 * d + 1
                for key, value in tmp_dic.items():
                    tmp_dic[key] = value + 1
                tmp_dic[d] = 0

        for idx, item in enumerate(sorted(ret_dic.items(), key=lambda item: (item[1], item[0]))):
            if idx == k - 1:
                return item[0]


class TestSolution(unittest.TestCase):
    def test_getKth(self):
        param50, param51, param52 = 1, 1000, 777
        param40, param41, param42 = 10, 20, 5
        param30, param31, param32 = 7, 11, 4
        param20, param21, param22 = 1, 1, 1
        param10, param11, param12 = 12, 15, 2

        solution = Solution()
Q        self.assertEqual(570, solution.getKth(param50, param51, param52))
        self.assertEqual(13, solution.getKth(param40, param41, param42))
        self.assertEqual(7, solution.getKth(param30, param31, param32))
        self.assertEqual(1, solution.getKth(param20, param21, param22))
        self.assertEqual(13, solution.getKth(param10, param11, param12))


if __name__ == '__main__':
    unittest.main()
