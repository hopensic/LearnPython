# Definition for a binary tree node.
import array
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



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


def build_list_from_tree_new(root: TreeNode):
    depth = cal_tree_depth(root)
    lst = [0] * (2 ** depth - 1)
    traverse(root, 0, lst)
    return lst


def traverse(node, index, lst):
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


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # lst = [3, 4, 5, 5, 4, None, 7]
        # return buildTree(lst)
        if (not t1 and not t2):
            return None
        a = build_list_from_tree_new(t1)
        print(a)
        b = build_list_from_tree_new(t2)
        print(b)
        c = []
        e = []
        na = len(a)
        nb = len(b)
        d = na
        if na < nb:
            d = na
            e = b[d:]
        elif na > nb:
            d = nb
            e = a[d:]

        for i in range(0, d):
            if (a[i] is not None or b[i] is not None):
                if a[i] is None:
                    a[i] = 0
                if b[i] is None:
                    b[i] = 0
                c.append(a[i] + b[i])
            else:
                c.append(None)
        if (na != nb):
            f = c + e
        else:
            f = c
        print(f)
        return buildTree(f)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]

    if not input:
        return None

    #获取列表中所有的结点
    inputValues = [s.strip() for s in input.split(',')]
    #根结点
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    #

    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)


    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()


    while True:
        try:
            line = next(lines)
            t1 = stringToTreeNode(line);
            line = next(lines)
            t2 = stringToTreeNode(line);

            ret = Solution().mergeTrees(t1, t2)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()