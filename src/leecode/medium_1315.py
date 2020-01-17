from datetime import datetime

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1315 ^medium ^tree ^dfs
name: ^(Sum of Nodes with Even-Valued Grandparent)
'''


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None or root.val is None:
            return 0
        return self.get_sumof_node(root, [])

    def get_sumof_node(self, node: TreeNode, lst: list):
        le = len(lst)
        sums = 0
        for i in range(le):
            lst[i] += 1
        if node.val % 2 == 0:
            lst.append(0)
        if lst.count(2) > 0:
            sums += node.val
        if node.left:
            sums += self.get_sumof_node(node.left, lst)
        if node.right:
            sums += self.get_sumof_node(node.right, lst)

        if len(lst) > 0:
            if lst[-1] == 0:
                lst.pop()
        for i in range(le):
            lst[i] -= 1
        return sums


t1 = datetime.now()
s = Solution()
root1 = '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
node = stringToTreeNode(root1)

print(s.sumEvenGrandparent(node))
t2 = datetime.now()
print(t2 - t1)
