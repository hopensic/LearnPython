# 根据列表构建二叉树
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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
