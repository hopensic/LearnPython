class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyLinkedList:

    def __init__(self):
        self.cur_len = 0
        self.head = None
        self.tail = None
        """
        Initialize your data structure here.
        """

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.cur_len - 1:
            return -1

        p = self.head
        n = 0
        while n < index:
            n += 1
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        node = LinkedNode(val)
        if self.cur_len == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.cur_len += 1
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

    def addAtTail(self, val: int) -> None:
        node = LinkedNode(val)
        if self.cur_len == 0:
            self.head = node
            self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        self.cur_len += 1
        """
        Append a node of value val to the last element of the linked list.
        """

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.cur_len:
            if index == 0:
                self.addAtHead(val)
            elif index == self.cur_len:
                self.addAtTail(val)
            else:
                p = self.head
                n = 0
                while n < index - 1:
                    n += 1
                    p = p.next
                node = LinkedNode(val)
                node.next = p.next
                p.next.pre = node
                node.pre = p
                p.next = node
                self.cur_len += 1

        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.cur_len:
            if index == 0:
                self.head = self.head.next
                if self.head:
                    self.head.pre = None
            elif index == self.cur_len - 1:
                self.tail = self.tail.pre
                if self.tail:
                    self.tail.next = None
            else:
                to_deleted = self.head
                n = 0
                while n < index:
                    n += 1
                    to_deleted = to_deleted.next
                to_deleted.pre.next = to_deleted.next
                to_deleted.next.pre = to_deleted.pre
            self.cur_len -= 1

        """
        Delete the index-th node in the linked list, if the index is valid.
        """


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtIndex(3, 0)
# obj.deleteAtIndex(2)
# obj.addAtHead(6)
# obj.addAtTail(4)
# print(obj.get(4))

# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(2, 0)
# print(obj.get(1))

obj.addAtHead(1)
obj.deleteAtIndex(0)