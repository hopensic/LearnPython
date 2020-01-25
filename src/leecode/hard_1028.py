from datetime import datetime
from leecode.common.common_class import TreeNode

'''
tag: ^1028 ^hard ^dfs
name: ^(Recover a Tree From Preorder Traversal)
'''


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 先找到第一个-， 有可能不存在
        i = S.find('-')
        if i == -1:
            return TreeNode(int(S))
        else:
            first_num = int(S[:i])
        cur_node = TreeNode(-1)
        root = TreeNode(first_num)
        nodelist = [(root.val, 0, root)]
        word = []
        while i < len(S):
            level = 0
            word.clear()
            while S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                word.append(S[i])
                i += 1
            num = int(''.join(word))
            nodelist.append((num, level, TreeNode(num)))
        stacks = []
        cur_lever = -1
        for num, level, node in nodelist:
            if level > cur_lever:
                cur_lever = level
                stacks.append((level, node))
                if cur_node.left is None:
                    cur_node.left = node
                    cur_node = cur_node.left
                else:
                    cur_node.right = node
                    cur_node = cur_node.right
                continue
            else:
                while True:
                    cur_lever, cur_node = stacks[-1]
                    if cur_lever + 1 == level:
                        break
                    else:
                        cur_lever, cur_node = stacks.pop()
                        continue
                cur_node.right = node
                cur_node = cur_node.right
                cur_lever = level
                stacks.append((level, node))

        return root


# arr1 = "1-2--3--4-5--6--7"
# arr1 = "1-2--3---4-5--6---7"
# arr1 = "1-401--349---90--88"
arr1 = "10-7--8"

t1 = datetime.now()
s = Solution()
print(s.recoverFromPreorder(arr1))
t2 = datetime.now()
print(t2 - t1)
