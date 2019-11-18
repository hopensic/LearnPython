# Definition for a binary tree node.
from leecode.common.commons import buildTree, TreeNode

d = {}
lst = []

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        d.clear()
        lst.clear()
        self.traverse(root)
        d[lst[0]] = lst[0]
        for x in lst[1:]:
            d[x] = d[x + 1] + x
        self.update(root)
        return root

    def traverse(self, node):
        if (not node):
            return
        self.traverse(node.right)
        lst.append(node.val)
        self.traverse(node.left)

    def update(self, node):
        if (not node):
            return
        self.update(node.right)
        node.val = d[node.val]
        self.update(node.left)


# treelist = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
treelist = [0, None, 1]
root_tree = buildTree(treelist)
print('-----')

solution = Solution()
solution.bstToGst(root_tree)
# solution.traverse(root_tree)
