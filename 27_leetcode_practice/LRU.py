class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRU:
    def __init__(self,capacity=0):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def _addtoHead(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        node.prev = self.head
        nxt.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._remove(node)
        self._addtoHead(node)
        return node.val

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.cache[key] = node
            self._remove(node)
            self._addtoHead(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.tail.prev
                self._remove(node)
                del self.cache[last.key]
            new_node = Node(key, val)
            self.cache[key] = new_node
            self._addtoHead(new_node)
        
