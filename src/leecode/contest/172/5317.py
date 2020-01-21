# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None
        res, _ = self.get_sub(root, target)
        return res

    def get_sub(self, node: TreeNode, target: int):
        if node.val == target:
            if node.left is None and node.right is None:
                return (None, 1)
            else:
                if node.left:
                    tree, is_need_delete = self.get_sub(node.left, target)
                    if is_need_delete == 1:
                        node.left = None
                    else:
                        node.left = tree

                if node.right:
                    tree, is_need_delete = self.get_sub(node.right, target)
                    if is_need_delete == 1:
                        node.right = None
                    else:
                        node.right = tree

                if node.left is None and node.right is None:
                    return (None, 1)
                else:
                    return (node, 0)
        else:
            if node.left:
                tree, is_need_delete = self.get_sub(node.left, target)
                if is_need_delete == 1:
                    node.left = None
                else:
                    node.left = tree
            if node.right:
                tree, is_need_delete = self.get_sub(node.right, target)
                if is_need_delete == 1:
                    node.right = None
                else:
                    node.right = tree
            return (node, 0)


nodes = '[1,2,null,2,null,2]'
tar = 2
root1 = stringToTreeNode(nodes)

s = Solution()
res = s.removeLeafNodes(root1, tar)
print(1)
