from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        iter_head = TreeNode(None)
        head = iter_head
        if root.left is not None:
            head = self.build_left_tree(root.left, root)
        if root.right is not None:
            root.right = self.build_right_tree(root.right)
        return head

    def build_left_tree(self, node, parent):
        # 代表是构造左子树
        new_left_tree_head = None
        # 如果左子树非空，构造左子数
        if node.left is not None:
            # 构造左子树
            new_left_tree = self.build_left_tree(node.left, node)
            new_left_tree_head = new_left_tree

            # 将新的左子数的最右子树设为parent
            while (True):
                if new_left_tree is None:
                    new_left_tree.right = parent
                    break;
        # 如果左子树空，将parent挂到左子数的右侧，并且将parent的左设为空
        else:
            node.right=parent
            parent.left = None


        if node.right is not None:
            node.right = self.build_right_tree(node.right)

        return new_left_tree_head

    def build_right_tree(self, node):
        new_left_tree_head = None

        if node.left is not None:
            # 构造左子树
            new_left_tree = self.build_left_tree(node.left, node)
            new_left_tree_head = new_left_tree
            # 将新的左子数的最右子树设为parent
            while (True):
                if new_left_tree is None:
                    new_left_tree.right = node
                    break;
            node.right = self.build_right_tree(node.right)
            # 如果左子树，将parent挂到左子数的右侧，并且将parent的左设为空
        else:
            node.right = parent
            parent.left = None

        if node.left is not None:
            return new_left_tree_head
        else:
            return node


lst = "[5,3,6,2,4,null,8,1,null,null,null,7,9]"
root = stringToTreeNode(lst)

s = Solution()
s.increasingBST(root)
