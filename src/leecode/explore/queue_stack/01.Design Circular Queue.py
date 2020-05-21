class MyCircularQueue:

    def __init__(self, k: int):
        self.queuesize = k
        self.lst = [None] * k
        self.head = -1
        self.tail = -1
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.head < 0:
            self.head = (self.head + 1) % self.queuesize
        self.tail = (self.tail + 1) % self.queuesize
        self.lst[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.lst[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.queuesize
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.head > -1:
            return self.lst[self.head]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.tail > -1:
            return self.lst[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.head < 0 and self.tail < 0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.head > -1 and self.tail > -1:
            if (self.tail + 1) % self.queuesize == self.head:
                return True
            else:
                return False
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
param_1 = obj.enQueue(4)
param_1 = obj.Rear()
param_1 = obj.enQueue(9)
param_2 = obj.deQueue()
param_2 = obj.Front()
param_2 = obj.deQueue()
param_2 = obj.deQueue()



param_1 = obj.Rear()
param_2 = obj.deQueue()
param_1 = obj.enQueue(5)
param_4 = obj.Rear()
param_2 = obj.deQueue()
param_2 = obj.Front()
param_2 = obj.deQueue()
param_2 = obj.deQueue()
param_2 = obj.deQueue()
