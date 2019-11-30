class MultiTreeNode:
    def __init__(self, lst: str, x=None):
        self.val = x  # 结点值
        self.child_list = []  # 子结点列表
        self.remain = lst

    # 添加一个孩子结点
    def add_child(self, node):
        self.child_list.append(node)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
