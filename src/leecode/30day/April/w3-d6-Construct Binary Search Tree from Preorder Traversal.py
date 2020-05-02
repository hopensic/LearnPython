import unittest
import bisect
from leecode.common.commons import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        left_lst, right_lst = [], []
        le = len(preorder)
        if le == 0:
            return None
        elif le == 1:
            return TreeNode(preorder[0])
        else:
            cur_root = TreeNode(preorder[0])
            if preorder[1] > preorder[0]:
                right_lst = preorder[1:]
            else:
                for i in preorder[1:]:
                    if i < preorder[0]:
                        left_lst.append(i)
                    else:
                        right_lst.append(i)
            if len(left_lst) > 0: cur_root.left = self.bstFromPreorder(left_lst)
            if len(right_lst) > 0: cur_root.right = self.bstFromPreorder(right_lst)
            return cur_root


class TestSolution(unittest.TestCase):
    def test_bstFromPreorder(self):
        # param = [8, 5, 1, 7, 10, 12]
        # param = [1, 3, 2]
        param = [10, 3, 19, 14]
        so = Solution()
        tree = so.bstFromPreorder(param)
        print(1)


if __name__ == '__main__':
    unittest.main()
