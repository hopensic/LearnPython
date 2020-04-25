class DeNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = DeNode(-1, -1), DeNode(-2, -2)
        self.dic = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # 如果在字典中，需要将key删除，双向链
        if key in self.dic:
            self.remove(self.dic[key])
        new_node = DeNode(key, value)
        # 将节点增加到链表头
        self.append(new_node)
        self.dic[key] = new_node
        # 如果大于容量，需要将尾部元素删除
        tail_node = self.tail.pre
        if len(self.dic) > self.capacity:
            self.remove(tail_node)
            del self.dic[tail_node.key]

    # 删除该节点的前后链
    def remove(self, node: DeNode):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

    # 将节点增加到头
    def append(self, node):
        p = self.head.next
        p.pre = node
        node.pre = self.head
        node.next = p
        self.head.next = node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(3, 3)
print(cache.get(2))
