from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

import unittest


class Solution:
    def kthSmallest(self, node: TreeNode, k: int) -> int:
        i = 0
        stacks = []
        while True:
            if node:
                stacks.append(node)
                node = node.left
            elif len(stacks) > 0:
                node = stacks.pop()
                i += 1
                if i == k:
                    return node.val
                node = node.right
            else:
                break

        return None


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
