# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from leecode.common.common_class import TreeNode


class Solution:
    dic = {}

    def allPossibleFBT(self, N: int):
        Solution.dic.clear()
        if N == 1:
            return [TreeNode(0)]
        if N % 2 == 0:
            return []
        Solution.dic[1] = [TreeNode(0)]

        for i in range(3, N + 1, 2):
            Solution.dic[i] = self.build_tree_list(i)
        return Solution.dic[N]

    # sub_tree_num 子数的数量
    def build_tree_list(self, sub_tree_num):
        sub_tree_num -= 1

        lst = [(i, sub_tree_num - i) for i in range(1, sub_tree_num, 2)]

        ret_lst = []
        for left, right in lst:
            for L in Solution.dic[left]:
                for R in Solution.dic[right]:
                    node = TreeNode(0)
                    node.left = L
                    node.right = R
                    ret_lst.append(node)

        Solution.dic[sub_tree_num + 1] = ret_lst
        return ret_lst


s = Solution()
a = s.allPossibleFBT(2)
print(a)
