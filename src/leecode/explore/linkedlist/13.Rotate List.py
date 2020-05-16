# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next or k == 0:
            return head

        # 找到第k个节点
        def find_k_node(pre: ListNode, h: ListNode):
            nonlocal k
            i = 1
            while h and i < k:
                h = h.next
                i += 1
            if h:
                while h.next:
                    h = h.next
                    pre = pre.next
                # 返回新链的头
                h.next = head
                dummy = pre
                while pre.next is not dummy:
                    pre = pre.next
                pre.next = None
                return dummy
            else:
                k %= (i - 1)
                if k == 0:
                    return head
                return find_k_node(head, head)

        return find_k_node(head, head)


# arr1 = '[1,2,3,4,5]'
# lst1 = stringToListNode(arr1)
# k = 2

# arr1 = '[0]'
# lst1 = stringToListNode(arr1)
# k = 4

# arr1 = '[0,1,2,3]'
# lst1 = stringToListNode(arr1)
# k = 5

# arr1 = '[0,1,2]'
# lst1 = stringToListNode(arr1)
# k = 4

arr1 = '[1,2,3,4,5]'
lst1 = stringToListNode(arr1)
k = 10

s = Solution()
print(s.rotateRight(lst1, k))
