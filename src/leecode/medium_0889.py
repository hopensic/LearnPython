from datetime import datetime

from leecode.common.common_class import TreeNode

'''
tag: ^889 ^medium ^tree
name: ^(Construct Binary Tree from Preorder and Postorder Traversal)
'''


class Solution:
    def constructFromPrePost(self, pre: list, post: list) -> TreeNode:
        post.reverse()
        def make_tree(left, right):
            root = TreeNode(left[0])
            if len(left) == 1:
                return root

            left_begin_index = right.index(left[1])
            # 中左右遍历的左树
            left_tree = left[1:1 + len(right) - left_begin_index]
            # 中右左遍历的左树
            left_tree_post = right[left_begin_index:]

            # 中左右遍历的右树
            right_tree = left[1 + len(right) - left_begin_index:]
            # 中右左遍历的右树
            right_tree_post = right[1:left_begin_index]

            if len(left_tree) > 0:
                root.left = make_tree(left_tree, left_tree_post)
            if len(right_tree) > 0:
                root.right = make_tree(right_tree, right_tree_post)

            return root

        r = make_tree(pre, post)

        return r


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]

t1 = datetime.now()
s = Solution()
print(s.constructFromPrePost(pre, post))
t2 = datetime.now()
print(t2 - t1)
