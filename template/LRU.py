#lru的模板
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #第一个内部操作，插入到头部
    def _add(self, node):
        nxt = self.head.next
        self.head.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = self.head

    #第二个内部操作，删除某节点
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #第三个操作，移动到头部
    def _move(self, node):
        self._remove(node)
        self._add(node)

    #对外操作，get是否有这个缓存信息
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move(node)
        return node.value

    #对外操作，put把一个key-value放进缓存里
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move(node)
        else:
            if len(self.cache) >= self.capacity:
                rm_node = self.tail.prev
                self._remove(rm_node)
                self.cache.pop(rm_node.key)
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

if __name__ == "__main__":
    lru = LRU(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # 1
    lru.put(3, 3)  # 淘汰 key=2
    print(lru.get(2))  # -1
    lru.put(4, 4)  # 淘汰 key=1
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4