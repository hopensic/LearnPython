from datetime import datetime
from leecode.common.official import stringToTreeNode
from leecode.common.common_class import TreeNode

'''
tag: ^0951 ^medium ^tree
name: ^(Flip Equivalent Binary Trees)
'''


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 and root2:
            if root1.val == root2.val:
                return (self.flipEquiv(root1.left, root2.left)
                        and (self.flipEquiv(root1.right, root2.right))) or (
                               self.flipEquiv(root1.left, root2.right) and (self.flipEquiv(root1.right, root2.left)))
            else:
                return False
        else:
            return False


root1 = '[1,2,3,4,5,6,null,null,null,7,8]'
root2 = '[1,3,2,null,6,4,5,null,null,null,null,8,7]'
node1 = stringToTreeNode(root1)
node2 = stringToTreeNode(root2)

t1 = datetime.now()
s = Solution()
print(s.flipEquiv(node1, node2))
t2 = datetime.now()
print(t2 - t1)
