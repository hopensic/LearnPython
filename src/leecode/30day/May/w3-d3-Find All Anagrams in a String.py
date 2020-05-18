from collections import deque, Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        left, res = 0, []
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s or len_p == 0:
            return []
        cur_counter = Counter()
        for i in range(len_s):
            if s[i] not in c:
                cur_counter.clear()
                left = i + 1
                continue
            cur_counter[s[i]] += 1
            if i - left == len_p - 1:
                if cur_counter == c:
                    res.append(left)
                cur_counter[s[left]] -= 1
                if cur_counter[s[left]] == 0:
                    del cur_counter[s[left]]
                left += 1
        return res


class TestSolution(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        param30, param31 = "aaaa", "aa"
        param20, param21 = "cbaebabacd", "abc"
        param10, param11 = "abab", "ab"

        solution = Solution()

        self.assertEqual([0, 1, 2], solution.findAnagrams(param30, param31))
        self.assertEqual([0, 6], solution.findAnagrams(param20, param21))
        self.assertEqual([0, 1, 2], solution.findAnagrams(param10, param11))


if __name__ == '__main__':
    unittest.main()
