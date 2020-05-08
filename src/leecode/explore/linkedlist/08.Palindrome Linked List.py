# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        new_head = loop_pointer = head
        n = 1
        while loop_pointer.next:
            n += 1
            loop_pointer = loop_pointer.next
        if n <= 3:
            return head.val == loop_pointer.val
        # 将前一半的链表反转
        num = int(n / 2) - 1
        while num > 0:
            to_transfer = head.next
            head.next = to_transfer.next
            to_transfer.next = new_head
            new_head = to_transfer
            num -= 1
        if n % 2 == 1:
            head = head.next.next
        else:
            head = head.next
        # 前半串和后半串进行对比
        while head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head=new_head.next
        return True


arr = '[1,2,2,1]'
lst = stringToListNode(arr)

s = Solution()
print(s.isPalindrome(lst))
