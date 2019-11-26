from leecode.common.commons import TreeNode


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]

    if not input:
        return None

    # 获取列表中所有的结点
    inputValues = [s.strip() for s in input.split(',')]
    # 根结点
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
