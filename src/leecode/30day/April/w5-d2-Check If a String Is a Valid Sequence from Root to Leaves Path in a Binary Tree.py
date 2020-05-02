from datetime import datetime
from leecode.common.official import stringToTreeNode

from leecode.common.common_class import TreeNode


class Solution:

    def isValidSequence(self, root: TreeNode, arr: list) -> bool:
        le = len(arr)

        def get_lef(t: TreeNode, cur_lev):
            if not t:
                return False

            if t.val != arr[cur_lev]:
                return False
            else:
                if cur_lev == le - 1:
                    if not t.left and not t.right:
                        return True
                    else:
                        return False
                else:
                    left = get_lef(t.left, cur_lev + 1)
                    if not left:
                        right = get_lef(t.right, cur_lev + 1)
                        return right
                    else:
                        return True

        return get_lef(root, 0)


root = '[0,1,0,0,1,0,null,null,1,0,0]'
tree = stringToTreeNode(root)
arr = [0, 1, 1]

t1 = datetime.now()
s = Solution()
print(s.isValidSequence(tree, arr))
t2 = datetime.now()
print(t2 - t1)
