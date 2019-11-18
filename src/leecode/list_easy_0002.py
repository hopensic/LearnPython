# Definition for singly-linked list.
from leecode.common.commons import ListNode


def build_listnodes(list1, list2):
    total_list = []
    root1 = ListNode(list1[0])
    list_node1 = root1
    for a in list1[1:]:
        list_node1.next = ListNode(a)
        list_node1 = list_node1.next

    root2 = ListNode(list2[0])
    list_node2 = root2
    for a in list2[1:]:
        list_node2.next = ListNode(a)
        list_node2 = list_node2.next
    total_list.append(root1)
    total_list.append(root2)
    return total_list




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        s1_new = "".join(str(x) for x in s1[::-1])
        s2_new = "".join(str(x) for x in s2[::-1])
        sum = int(s1_new) + int(s2_new)
        s = str(sum)
        root = ListNode(s[-1])
        list_node1 = root
        for a in s[-2::-1]:
            list_node1.next = ListNode(a)
            list_node1 = list_node1.next

        return root


twolist = build_listnodes([2, 4, 3], [5, 6, 4])
print('--------------------')
s = Solution()
ret = s.addTwoNumbers(twolist[0], twolist[1])
print('--------------------')
