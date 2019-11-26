# Definition for a binary tree node.

from leecode.common.commons import TreeNode, buildTree


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int):
        t = root
        while (True):
            if (val < t.val):
                if (not t.left):
                    t.left = TreeNode(val)
                    return root
                t = t.left
            else:
                if (not t.right):
                    t.right = TreeNode(val)
                    return root
                t = t.right


so = Solution()

lst = [4, 2, 7, 1, 3]

root = buildTree(lst)

so.insertIntoBST(root, 5)
print('----------')
