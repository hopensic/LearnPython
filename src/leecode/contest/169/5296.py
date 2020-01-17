# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list:
        res = []
        list1 = self.getList(root1)
        list2 = self.getList(root2)
        le1 = len(list1)
        le2 = len(list2)
        print(list1)
        print(list2)

        if le1 == 0:
            return list2
        if le2 == 0:
            return list1

        i = j = 0
        while True:
            if i == le1 or j == le2:
                break
            if list1[i] > list2[j]:
                res.append(list2[j])
                j += 1
            elif list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list1[i])
                res.append(list2[j])
                i += 1
                j += 1
        if i == le1:
            res.extend(list2[j:])
        if j == le2:
            res.extend(list1[i:])

        return res

    def getList(self, node):
        res = []
        current = node
        stacks = []  # initialize stack
        while True:
            if current is not None:
                stacks.append(current)
                current = current.left
            elif stacks:
                current = stacks.pop()
                res.append(current.val)
                current = current.right

            else:
                break
        return res


s1 = "[2,1,4]"
s2 = "[1,0,3]"

node1 = stringToTreeNode(s1)
node2 = stringToTreeNode(s2)

s = Solution()
print(s.getAllElements(node1, node2))
