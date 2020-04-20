from datetime import datetime
from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1382 ^medium ^bst ^tree
name: ^(Balance a Binary Search Tree)
'''


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build_tree(lst: list):
            le = len(lst)
            if le == 0:
                return
            if le == 1:
                return TreeNode(lst[0])
            middle = int(le / 2)
            r = TreeNode(lst[middle])
            r.left = build_tree(lst[0:middle])
            r.right = build_tree(lst[middle + 1:])
            return r

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

        res.sort()
        tree = build_tree(res)
        return tree


arr1 = '[2,1,3,null,null,null,4]'
tree = stringToTreeNode(arr1)

t1 = datetime.now()
s = Solution()
print(s.balanceBST(tree))
t2 = datetime.now()
print(t2 - t1)
