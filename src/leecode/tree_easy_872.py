# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_lst(root1) == self.get_lst(root2)

    def get_lst(self, node: TreeNode):
        ret_lst = []
        stacks = [node]
        while len(stacks) > 0:
            poped = stacks.pop()
            if poped.left is None and poped.right is None:
                ret_lst.append(poped.val)
            else:
                if poped.right is not None:
                    stacks.append(poped.right)
                if poped.left is not None:
                    stacks.append(poped.left)
        return ret_lst


s1 = '[3,5,1,6,2,9,8,null,null,7,4]'
s2 = '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'

root1 = stringToTreeNode(s1)
root2 = stringToTreeNode(s2)

s = Solution()
print(s.leafSimilar(root1, root2))
