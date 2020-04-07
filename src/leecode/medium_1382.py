from datetime import datetime
from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1382 ^medium ^bst
name: ^(Balance a Binary Search Tree)
'''


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        stacks = []
        if root:
            stacks.append(root)
            while len(stacks) > 0:
                poped = stacks.pop()
                res.append(poped.val)
                if poped.right:
                    stacks.append(poped.right)
                if poped.left:
                    stacks.append(poped.left)

        return res


arr1 = '[2,1,3,null,null,null,4]'
tree = stringToTreeNode(arr1)

t1 = datetime.now()
s = Solution()
print(s.balanceBST(tree))
t2 = datetime.now()
print(t2 - t1)
