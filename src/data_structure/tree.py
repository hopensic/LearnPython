from leecode.common.common_class import TreeNode


class Tree:

    # 前序遍归遍历二叉树(前序也就是根结点是最先访问的)-递归
    @staticmethod
    def preorder_traversal_with_recursion(node: TreeNode):
        res = []
        if node:
            res.append(node.val)
            if node.left:
                res.extend(Tree.preorder_traversal_with_recursion(node.left))
            if node.right:
                res.extend(Tree.preorder_traversal_with_recursion(node.right))
            return res
        return res

    # 前序遍归-非递归
    @staticmethod
    def preorder_traversal_without_recursion(node: TreeNode):
        res = []
        stacks = []
        if node:
            stacks.append(node)
            while len(stacks) > 0:
                poped = stacks.pop()
                res.append(poped.val)
                if poped.right:
                    stacks.append(poped.right)
                if poped.left:
                    stacks.append(poped.left)
            return res
        return res

    '''
    -----------------------------------------------------------------------------------------
    '''

    # 中序遍归遍历二叉树(根结点在中间访问)-递归
    @staticmethod
    def inorder_traversal_with_recursion(node: TreeNode):
        res = []
        if node:
            if node.left:
                res.extend(Tree.inorder_traversal_with_recursion(node.left))
            res.append(node.val)
            if node.right:
                res.extend(Tree.inorder_traversal_with_recursion(node.right))
            return res
        return res

    # 中序遍归-非递归
    @staticmethod
    def inorder_traversal_without_recursion(node: TreeNode):
        res = []
        stacks = []
        while True:
            if node:
                stacks.append(node)
                node = node.left
            elif len(stacks) > 0:
                node = stacks.pop()
                res.append(node.val)
                node = node.right
            else:
                break

        return res

    '''
    -----------------------------------------------------------------------------------------
    '''

    # 后序遍归遍历二叉树(后也就是根结点是最后访问的)-递归
    @staticmethod
    def postorder_traversal_with_recursion(node: TreeNode):
        res = []
        if node:
            if node.left:
                res.extend(Tree.postorder_traversal_with_recursion(node.left))
            if node.right:
                res.extend(Tree.postorder_traversal_with_recursion(node.right))
            res.append(node.val)
            return res
        return res

    @staticmethod
    # 返回栈顶元素
    def get_top_stack(stacks):
        if len(stacks) > 0:
            return stacks[-1]
        return None

    # 后序遍归-非递归
    @staticmethod
    def postorder_traversal_without_recursion(node: TreeNode):
        res = []
        stacks = []
        if node is None:
            return res
        while True:
            while node:
                if node.right:
                    stacks.append(node.right)
                stacks.append(node)
                node = node.left

            node = stacks.pop()

            if node.right and node.right == Tree.get_top_stack(stacks):
                stacks.pop()
                stacks.append(node)
                node = node.right
            else:
                res.append(node.val)
                node = None
            if len(stacks) <= 0:
                break

        return res
