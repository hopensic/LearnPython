from leecode.common.commons import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        return self.build_tree(t1, t2)

    def build_tree(self, t1, t2):
        if t1 is not None or t2 is not None:
            node = TreeNode(0)
            v1, v2 = 0, 0
            if t1 is not None:
                v1 = t1.val
            if t2 is not None:
                v2 = t2.val
            x = v1 + v2
            node.val = v1 + v2

            if t1 is None:
                # node.left = self.build_tree(None, t2.left)
                # node.left = self.build_tree(None, t2.right)
                # node.right=t2
                return t2

            elif t2 is None:
                # node.right = self.build_tree(t1.left, None)
                # node.right = self.build_tree(t1.left, None)
                # node.left = t1
                return t1
            else:
                node.left = self.build_tree(t1.left, t2.left)
                node.right = self.build_tree(t1.right, t2.right)
            return node
        else:
            return None


# t1 = buildTree([1, 3, 2, 5])
# t2 = buildTree([2, 1, 3, None, 4, None, 7])

# t1 = buildTree([3, 4, 5, 1, 2, None, None, 0])
# t2 = buildTree([4, 1, 2])

# t1 = buildTree([1, 2, None, 3])
# t2 = buildTree([1, None, 2, None, None, None, 3])


t1 = stringToTreeNode('[1,2,null,3]')
t2 = stringToTreeNode('[4,null,7,null,8]')

so = Solution()
r = so.mergeTrees(t1, t2)
print('---------')
