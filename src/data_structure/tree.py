import unittest

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
前序遍归遍历二叉树(前序也就是根结点是最先访问的)
应该是1-

'''


def preorder_traversal_with_recursion(node: TreeNode):
    print(1)
    return 1


class Test_Data_Structure_Tree(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        node_str = '[1,2,3,4,5,6,7]'
        Test_Data_Structure_Tree.node = stringToTreeNode(node_str)

    def test_preorder_with_recursion(self):
        a = preorder_traversal_with_recursion(self.node)
        self.assertEqual(1, a)
