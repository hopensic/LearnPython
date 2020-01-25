import unittest
from leecode.common.official import stringToTreeNode
from data_structure.tree import Tree


# def setUpModule():
#     # global a
#     # a = 12
#     print("Setup Module")
#
#
# def tearDownModule():
#     print("Closing Module")


class Test_Data_Structure_Tree(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.node1 = stringToTreeNode('[]')
        cls.node2 = stringToTreeNode('[1]')
        cls.node3 = stringToTreeNode('[1,2]')
        cls.node4 = stringToTreeNode('[1,2,null,3]')
        cls.node5 = stringToTreeNode('[1,2,null,null,4]')
        cls.node6 = stringToTreeNode('[1,2,null,3,4]')
        cls.node7 = stringToTreeNode('[1,null,3]')
        cls.node8 = stringToTreeNode('[1,null,3,4]')
        cls.node9 = stringToTreeNode('[1,null,3,null,5]')
        cls.node10 = stringToTreeNode('[1,2,3,4,5,6,7]')
        cls.node11 = stringToTreeNode('[1,2,3,null,5,6]')
        cls.node12 = stringToTreeNode('[1,2,3,4,null,null,7]')
        cls.node13 = stringToTreeNode('[1,2,3,4,null,7,null]')
        cls.node14 = stringToTreeNode('[1,2,3,null,4,null,6]')

    # 先序遍历(递归)
    def test_preorder_traversal_with_recursion(self):
        self.assertEqual([], Tree.preorder_traversal_with_recursion(self.node1))
        self.assertEqual([1], Tree.preorder_traversal_with_recursion(self.node2))
        self.assertEqual([1, 2], Tree.preorder_traversal_with_recursion(self.node3))
        self.assertEqual([1, 2, 3], Tree.preorder_traversal_with_recursion(self.node4))
        self.assertEqual([1, 2, 4], Tree.preorder_traversal_with_recursion(self.node5))
        self.assertEqual([1, 2, 3, 4], Tree.preorder_traversal_with_recursion(self.node6), )
        self.assertEqual([1, 3], Tree.preorder_traversal_with_recursion(self.node7))
        self.assertEqual([1, 3, 4], Tree.preorder_traversal_with_recursion(self.node8))
        self.assertEqual([1, 3, 5], Tree.preorder_traversal_with_recursion(self.node9))
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], Tree.preorder_traversal_with_recursion(self.node10))
        self.assertEqual([1, 2, 5, 3, 6], Tree.preorder_traversal_with_recursion(self.node11))
        self.assertEqual([1, 2, 4, 3, 7], Tree.preorder_traversal_with_recursion(self.node12))
        self.assertEqual([1, 2, 4, 3, 7], Tree.preorder_traversal_with_recursion(self.node13))
        self.assertEqual([1, 2, 4, 3, 6], Tree.preorder_traversal_with_recursion(self.node14))

    # 先序遍历(非递归)
    def test_preorder_without_recursion(self):
        self.assertEqual([], Tree.preorder_traversal_without_recursion(self.node1))
        self.assertEqual([1], Tree.preorder_traversal_without_recursion(self.node2))
        self.assertEqual([1, 2], Tree.preorder_traversal_without_recursion(self.node3))
        self.assertEqual([1, 2, 3], Tree.preorder_traversal_without_recursion(self.node4))
        self.assertEqual([1, 2, 4], Tree.preorder_traversal_without_recursion(self.node5))
        self.assertEqual([1, 2, 3, 4], Tree.preorder_traversal_without_recursion(self.node6), )
        self.assertEqual([1, 3], Tree.preorder_traversal_without_recursion(self.node7))
        self.assertEqual([1, 3, 4], Tree.preorder_traversal_without_recursion(self.node8))
        self.assertEqual([1, 3, 5], Tree.preorder_traversal_without_recursion(self.node9))
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], Tree.preorder_traversal_without_recursion(self.node10))
        self.assertEqual([1, 2, 5, 3, 6], Tree.preorder_traversal_without_recursion(self.node11))
        self.assertEqual([1, 2, 4, 3, 7], Tree.preorder_traversal_without_recursion(self.node12))
        self.assertEqual([1, 2, 4, 3, 7], Tree.preorder_traversal_without_recursion(self.node13))
        self.assertEqual([1, 2, 4, 3, 6], Tree.preorder_traversal_without_recursion(self.node14))

    # 中序遍历(递归)

    def test_inorder_traversal_with_recursion(self):
        self.assertEqual([], Tree.inorder_traversal_with_recursion(self.node1))
        self.assertEqual([1], Tree.inorder_traversal_with_recursion(self.node2))
        self.assertEqual([2, 1], Tree.inorder_traversal_with_recursion(self.node3))
        self.assertEqual([3, 2, 1], Tree.inorder_traversal_with_recursion(self.node4))
        self.assertEqual([2, 4, 1], Tree.inorder_traversal_with_recursion(self.node5))
        self.assertEqual([3, 2, 4, 1], Tree.inorder_traversal_with_recursion(self.node6))
        self.assertEqual([1, 3], Tree.inorder_traversal_with_recursion(self.node7))
        self.assertEqual([1, 4, 3], Tree.inorder_traversal_with_recursion(self.node8))
        self.assertEqual([1, 3, 5], Tree.inorder_traversal_with_recursion(self.node9))
        self.assertEqual([4, 2, 5, 1, 6, 3, 7], Tree.inorder_traversal_with_recursion(self.node10))
        self.assertEqual([2, 5, 1, 6, 3], Tree.inorder_traversal_with_recursion(self.node11))
        self.assertEqual([4, 2, 1, 3, 7], Tree.inorder_traversal_with_recursion(self.node12))
        self.assertEqual([4, 2, 1, 7, 3], Tree.inorder_traversal_with_recursion(self.node13))
        self.assertEqual([2, 4, 1, 3, 6], Tree.inorder_traversal_with_recursion(self.node14))

        # 中序递归遍历(非递归)

    # 中序遍历(非递归)
    def test_inorder_traversal_without_recursion(self):
        self.assertEqual([], Tree.inorder_traversal_without_recursion(self.node1))
        self.assertEqual([1], Tree.inorder_traversal_without_recursion(self.node2))
        self.assertEqual([2, 1], Tree.inorder_traversal_without_recursion(self.node3))
        self.assertEqual([3, 2, 1], Tree.inorder_traversal_without_recursion(self.node4))
        self.assertEqual([2, 4, 1], Tree.inorder_traversal_without_recursion(self.node5))
        self.assertEqual([3, 2, 4, 1], Tree.inorder_traversal_without_recursion(self.node6))
        self.assertEqual([1, 3], Tree.inorder_traversal_without_recursion(self.node7))
        self.assertEqual([1, 4, 3], Tree.inorder_traversal_without_recursion(self.node8))
        self.assertEqual([1, 3, 5], Tree.inorder_traversal_without_recursion(self.node9))
        self.assertEqual([4, 2, 5, 1, 6, 3, 7], Tree.inorder_traversal_without_recursion(self.node10))
        self.assertEqual([2, 5, 1, 6, 3], Tree.inorder_traversal_without_recursion(self.node11))
        self.assertEqual([4, 2, 1, 3, 7], Tree.inorder_traversal_without_recursion(self.node12))
        self.assertEqual([4, 2, 1, 7, 3], Tree.inorder_traversal_without_recursion(self.node13))
        self.assertEqual([2, 4, 1, 3, 6], Tree.inorder_traversal_without_recursion(self.node14))

    # 后序遍历(递归)
    def test_postorder_traversal_with_recursion(self):
        self.assertEqual([], Tree.postorder_traversal_with_recursion(self.node1))
        self.assertEqual([1], Tree.postorder_traversal_with_recursion(self.node2))
        self.assertEqual([2, 1], Tree.postorder_traversal_with_recursion(self.node3))
        self.assertEqual([3, 2, 1], Tree.postorder_traversal_with_recursion(self.node4))
        self.assertEqual([4, 2, 1], Tree.postorder_traversal_with_recursion(self.node5))
        self.assertEqual([3, 4, 2, 1], Tree.postorder_traversal_with_recursion(self.node6), )
        self.assertEqual([3, 1], Tree.postorder_traversal_with_recursion(self.node7))
        self.assertEqual([4, 3, 1], Tree.postorder_traversal_with_recursion(self.node8))
        self.assertEqual([5, 3, 1], Tree.postorder_traversal_with_recursion(self.node9))
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], Tree.postorder_traversal_with_recursion(self.node10))
        self.assertEqual([5, 2, 6, 3, 1], Tree.postorder_traversal_with_recursion(self.node11))
        self.assertEqual([4, 2, 7, 3, 1], Tree.postorder_traversal_with_recursion(self.node12))
        self.assertEqual([4, 2, 7, 3, 1], Tree.postorder_traversal_with_recursion(self.node13))
        self.assertEqual([4, 2, 6, 3, 1], Tree.postorder_traversal_with_recursion(self.node14))

        # 后序遍历(非递归)
    def test_postorder_traversal_without_recursion(self):
        self.assertEqual([], Tree.postorder_traversal_without_recursion(self.node1))
        self.assertEqual([1], Tree.postorder_traversal_without_recursion(self.node2))
        self.assertEqual([2, 1], Tree.postorder_traversal_without_recursion(self.node3))
        self.assertEqual([3, 2, 1], Tree.postorder_traversal_without_recursion(self.node4))
        self.assertEqual([4, 2, 1], Tree.postorder_traversal_without_recursion(self.node5))
        self.assertEqual([3, 4, 2, 1], Tree.postorder_traversal_without_recursion(self.node6), )
        self.assertEqual([3, 1], Tree.postorder_traversal_without_recursion(self.node7))
        self.assertEqual([4, 3, 1], Tree.postorder_traversal_without_recursion(self.node8))
        self.assertEqual([5, 3, 1], Tree.postorder_traversal_without_recursion(self.node9))
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], Tree.postorder_traversal_without_recursion(self.node10))
        self.assertEqual([5, 2, 6, 3, 1], Tree.postorder_traversal_without_recursion(self.node11))
        self.assertEqual([4, 2, 7, 3, 1], Tree.postorder_traversal_without_recursion(self.node12))
        self.assertEqual([4, 2, 7, 3, 1], Tree.postorder_traversal_without_recursion(self.node13))
        self.assertEqual([4, 2, 6, 3, 1], Tree.postorder_traversal_without_recursion(self.node14))