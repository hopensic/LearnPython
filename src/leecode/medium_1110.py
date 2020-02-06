from datetime import datetime
from leecode.common.official import stringToTreeNode
from leecode.common.common_class import TreeNode

'''
tag: ^1110 ^medium ^tree ^dfs
name: ^(Delete Nodes And Return Forest)
'''


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list) -> list:
        dic = {v: v for v in to_delete}
        res = []
        if root is None:
            return []

        # sub_dir 代表左子树或右子树(0:左子树; １:右子树）
        def get_sub(node: TreeNode, parent: TreeNode, sub_dir: int):
            nonlocal dic
            nonlocal res
            k = dic.get(node.val, 0)
            if k > 0:
                if node.left:
                    res.append(node.left)
                    get_sub(node.left, node, 0)
                if node.right:
                    res.append(node.right)
                    get_sub(node.right, node, 1)
                if sub_dir:
                    parent.right = None
                else:
                    parent.left = None
            else:
                if node.left:
                    get_sub(node.left, node, 0)
                if node.right:
                    get_sub(node.right, node, 1)

        head = TreeNode(-1)
        head.left = root
        get_sub(root, head, 0)
        res.append(root)
        return [node for node in res if node.val not in dic]


arr1 = '[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]'
node = stringToTreeNode(arr1)
to_delete = [3, 5, 6]

t1 = datetime.now()
s = Solution()
print(s.delNodes(node, to_delete))
t2 = datetime.now()
print(t2 - t1)
