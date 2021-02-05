# 根据列表构建二叉树
from leecode.common.common_class import TreeNode


def buildTree(treelist):
    # 构建根元素
    tree_dic = {}
    max_len = len(treelist)
    root = 0
    stack = [root]
    root_tree = TreeNode(treelist[root])
    tree_dic[root] = root_tree
    while True:
        poped = stack.pop()
        tree = tree_dic[poped]
        right = poped * 2 + 2
        left = poped * 2 + 1
        if (right < max_len and treelist[right] != None):
            right_tree = TreeNode(treelist[right])
            tree.right = right_tree
            tree_dic[right] = right_tree
            stack.append(right)
        if (left < max_len and treelist[left] != None):
            left_tree = TreeNode(treelist[left])
            tree.left = left_tree
            tree_dic[left] = left_tree
            stack.append(left)
        if (len(stack) == 0):
            break
    return root_tree


# 根据二叉树构建列表
def build_list_from_tree(root):
    lst = []
    tmp_list = []
    tmp_list.append(root)
    while (True):
        if (len(tmp_list) == 0):
            break
        r = tmp_list.pop();
        if r:
            lst.append(r.val)
            tmp_list.insert(0, r.left)
            tmp_list.insert(0, r.right)
        else:
            lst.append(0)

    return lst


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




def build_list_from_tree_new(root: TreeNode):
    depth = cal_tree_depth(root)
    lst = [None] * (2 ** depth - 1)
    traverse(root, 0, lst)
    return lst


def traverse(node: TreeNode, index: int, lst: list):
    if (node):
        lst[index] = node.val
        if (node.left):
            traverse(node.left, index * 2 + 1, lst)
        if (node.right):
            traverse(node.right, index * 2 + 2, lst)


# 计算树的深度
def cal_tree_depth(root):
    if not root:
        return 0
    left = 1 + cal_tree_depth(root.left)
    right = 1 + cal_tree_depth(root.right)
    if left > right:
        return left
    else:
        return right
