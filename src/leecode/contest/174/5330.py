from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums = 0
        stacks = []
        if root:
            stacks.append(root)
            while len(stacks) > 0:
                poped = stacks.pop()
                sums += poped.val
                if poped.right:
                    stacks.append(poped.right)
                if poped.left:
                    stacks.append(poped.left)
        dic = set()

        if root:
            self.get_sub(root, dic)
        res = 0
        for d in dic:
            tmp = d * (sums - d)

            if tmp > res:
                res = tmp
        return res % (10 ** 9 + 7)

    def get_sub(self, node, subdic):
        if node:
            left = 0
            right = 0
            sums = 0
            sums += node.val
            if node.left:
                sums += self.get_sub(node.left, subdic)
            if node.right:
                sums += self.get_sub(node.right, subdic)
            subdic.add(sums)
            return sums
        else:
            return 0


arr = '[2,3,9,10,7,8,6,5,4,11,1]'
node = stringToTreeNode(arr)

s = Solution()
print(s.maxProduct(node))
