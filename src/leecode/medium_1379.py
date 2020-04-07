from datetime import datetime

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1379 ^medium ^tree
name: ^(Find a Corresponding Node of a Binary Tree in a Clone of That Tree)
'''


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        v = target.val
        stacks = []
        if cloned:
            stacks.append(cloned)
            while len(stacks) > 0:
                poped = stacks.pop()
                if poped.val == v:
                    return poped
                if poped.right:
                    stacks.append(poped.right)
                if poped.left:
                    stacks.append(poped.left)
        return None


arr = '[1,2,3,4,5,6,7,8,9,10]'
original = stringToTreeNode(arr)
cloned = stringToTreeNode(arr)
target = TreeNode(5)

t1 = datetime.now()
s = Solution()
res = s.getTargetCopy(original, cloned, target)
print(res)
t2 = datetime.now()
print(t2 - t1)
