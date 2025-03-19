class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.l = Node(-1, -1)
        self.r = Node(-1, -1)
        self.l.next = self.r
        self.r.prev = self.l
        self.cache = {}

    def remove(self, node)-> None:
        prv, nxt= node.prev, node.next
        prv.next, nxt.prev= nxt, prv

    def insert(self, node) -> None:
        prv, nxt = self.r.prev, self.r
        prv.next = nxt.prev = node
        node.next, node.prev=nxt, prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
           lru=self.l.next
           self.remove(lru)
           del self.cache[lru.key]
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)