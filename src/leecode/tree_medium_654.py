from leecode.common.commons import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: list):
        if len(nums) == 0:
            return None
        idx = nums.index(max(nums))
        node = TreeNode(nums[idx])
        node.left = left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return node


lst = [3, 2, 1, 6, 0, 5]
s = Solution()
r = s.constructMaximumBinaryTree(lst)
print('-----------')
