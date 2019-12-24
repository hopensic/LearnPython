# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        Solution.sum = 0
        if root.left:
            self.get_sumof_node_and_val(root.left)
        if root.right:
            self.get_sumof_node_and_val(root.right)
        return Solution.sum

    # get both sum of number of node and sum of val
    def get_sumof_node_and_val(self, node: TreeNode):
        if node.left is None and node.right is None:
            Solution.sum += abs(node.val - 1)
            return node.val, 1
        else:
            left_sum_of_val = 0
            left_sum_of_node = 0
            right_sum_of_val = 0
            right_sum_of_node = 0

            if node.left is not None:
                left_sum_of_val, left_sum_of_node = self.get_sumof_node_and_val(node.left)
            if node.right is not None:
                right_sum_of_val, right_sum_of_node = self.get_sumof_node_and_val(node.right)
            Solution.sum += abs(
                (left_sum_of_val + right_sum_of_val + node.val) -
                (left_sum_of_node + right_sum_of_node + 1))
            return left_sum_of_val + right_sum_of_val + node.val, left_sum_of_node + right_sum_of_node + 1


lst = '[0,0,0,0,4,2,0,null,null,0,null,null,3]'
node = stringToTreeNode(lst)

s = Solution()
print(s.distributeCoins(node))
