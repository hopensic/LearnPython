from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        left, res = 0, []
        len_p = len(s1)
        len_s = len(s2)
        if len_p > len_s:
            return False
        cur_counter = Counter()
        for i in range(len_s):
            if s2[i] not in c:
                cur_counter.clear()
                left = i + 1
                continue
            cur_counter[s2[i]] += 1
            if i - left == len_p - 1:
                if cur_counter == c:
                    return True
                cur_counter[s2[left]] -= 1
                if cur_counter[s2[left]] == 0:
                    del cur_counter[s2[left]]
                left += 1
        return False


class TestSolution(unittest.TestCase):
    def test_checkInclusion(self):
        param30, param31 = "ab", "eidbaooo"
        param20, param21 = "ab", "eidboaoo"
        param10, param11 = "abab", "ab"

        solution = Solution()

        self.assertEqual(True, solution.checkInclusion(param30, param31))
        self.assertEqual(False, solution.checkInclusion(param20, param21))
        self.assertEqual(False, solution.checkInclusion(param10, param11))


if __name__ == '__main__':
    unittest.main()
