from collections import defaultdict, deque
from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


string = "[4,2,7,1,3]"
root = stringToTreeNode(string)
val = 2

s1 = Solution()
t = s1.searchBST(root, val)
print(t)
