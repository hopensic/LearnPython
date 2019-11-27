from collections import deque

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode(None)
        pre = head
        current = root
        deq = deque()
        while (True):
            if current is not None:
                deq.append(current)
                current = current.left
            elif len(deq) > 0:
                current = deq.pop()
                node = TreeNode(current.val)
                head.right = node
                head = head.right
                current = current.right
            else:
                break;

        return pre.right


lst = "[5,3,6,2,4,null,8,1,null,null,null,7,9]"
root = stringToTreeNode(lst)

s = Solution()
r = s.increasingBST(root)
print(r)
