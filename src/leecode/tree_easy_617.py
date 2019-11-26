from leecode.common.commons import TreeNode, buildTree, build_list_from_tree_new


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
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
            f=c

        # for x, y in zip_longest(a, b):
        #     if (x is not None or y is not None):
        #         if x is None:
        #             x = 0
        #         if y is None:
        #             y = 0
        #         c.append(x + y)
        #     else:
        #         c.append(None)
        print(f)
        return buildTree(f)


t1 = buildTree([1, 3, 2, 5])
t2 = buildTree([2, 1, 3, None, 4, None, 7])

# t1 = buildTree([3, 4, 5, 1, 2, None, None, 0])
# t2 = buildTree([4, 1, 2])

# t1 = buildTree([1, 2, None, 3])
# t2 = buildTree([1, None, 2, None, None, None, 3])

so = Solution()
r = so.mergeTrees(t1, t2)
print('---------')
