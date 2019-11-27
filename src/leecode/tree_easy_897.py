# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        self.build_increase_tree(root)

        first_node = root
        pre_right = root

        while first_node.right:
            pre_right=first_node
            first_node=first_node.right

            if first_node.left:
                new_left_parent2=self.build_increase_tree(first_node.left,first_node)
                pre_right.right=new_left_parent2



        if root.left:
            new_left_parent = self.build_increase_tree(root.left,root)

    def build_increase_tree(self,node,parent=None):
        head = node
        if node.left:
            self.build_increase_tree(node.left,node)
            node.left=None
        if node.right:
            while True:
                node = node.right
                if node.left:
                    self.build_increase_tree(node.left,node)


        node.right=parent







l = "[5,3,6,2,4,null,8,1,null,null,null,7,9]"
root =stringToTreeNode(l)

s = Solution()
s.increasingBST(root)