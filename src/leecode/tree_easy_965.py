from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return []
        root_value = root.val
        stack = []
        stack.append(root)
        while True:
            if len(stack) == 0:
                break
            poped = stack.pop()
            if root_value != poped.val:
                return False;
            if poped.right:
                stack.append(poped.right)
            if poped.left:
                stack.append(poped.left)
        return True


lst2 = '[1,1,1,1,1,null,1]'
root = stringToTreeNode(lst2)

s = Solution()

print(s.isUnivalTree(root))
