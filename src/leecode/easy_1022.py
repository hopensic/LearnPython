from datetime import datetime
from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1022 ^easy ^tree
name: ^(Sum of Root To Leaf Binary Numbers)
'''


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        stacks = []
        def get_sum(t: TreeNode):
            stacks.append(str(t.val))
            if not t.right and not t.left:
                res.append(int(''.join(stacks), 2))
                stacks.pop()
                return

            if t.left:
                get_sum(t.left)
            if t.right:
                get_sum((t.right))
            stacks.pop()

        get_sum(root)

        return sum(res)


arr1 = '[1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1]'
tree = stringToTreeNode(arr1)
t1 = datetime.now()
s = Solution()
print(s.sumRootToLeaf(tree))
t2 = datetime.now()
print(t2 - t1)
