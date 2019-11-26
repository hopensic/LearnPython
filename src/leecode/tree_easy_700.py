# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from leecode.common.official import stringToTreeNode, TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while True:
            if not root:
                return None
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right


lst = '[4, 2, 7, 1, 3]'
root = stringToTreeNode(lst)

s = Solution()
r = s.searchBST(root, 5)
print('--------')
