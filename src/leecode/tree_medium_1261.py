from collections import deque

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        self.t = set()
        self.r = root
        self.r.val = 0
        self.t.add(self.r.val)
        self.build_tree(self.r)

    def build_tree(self, node: TreeNode):
        deq = deque()
        deq.append(node)
        while len(deq) > 0:
            poped = deq.pop()
            if poped.left:
                poped.left.val = poped.val * 2 + 1
                deq.append(poped.left)
                self.t.add(poped.left.val)
            if poped.right:
                poped.right.val = poped.val * 2 + 2
                deq.append(poped.right)
                self.t.add(poped.right.val)

    def find(self, target: int) -> bool:
        if target in self.t:
            return True
        else:
            return False
        # lt = [self.r]
        # while len(lt) > 0:
        #     poped = lt.pop()
        #     if poped.val == target:
        #         return True
        #     if poped.left:
        #         lt.append(poped.left)
        #     if poped.right:
        #         lt.append(poped.right)
        # return False


lst = '[-1, -1, -1, -1, -1]'
root2 = stringToTreeNode(lst)

findelements = FindElements(root2)
print(findelements.find(4))
