# Definition for a binary tree node.

from leecode.common.commons import buildTree, TreeNode


class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if (root == None):
            return sum
        if root.val < L:
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val == L:
            sum += L
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val > L and root.val < R:
            sum += root.val
            sum += self.rangeSumBST(root.left, L, R)
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val == R:
            sum += R
            sum += self.rangeSumBST(root.left, L, R)
        else:
            sum += self.rangeSumBST(root.left, L, R)

        return sum


treelist = [10, 5, 15, 3, 7, None, 18]
# treelist = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
root_tree = buildTree(treelist)
print('-----')

solution = Solution()
print(solution.rangeSumBST(root_tree, 7, 15))
