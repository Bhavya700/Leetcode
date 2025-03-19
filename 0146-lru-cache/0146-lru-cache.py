
class LRUCache:    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dd = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dd:
            self.dd.move_to_end(key)
            return self.dd[key]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.dd:
            self.dd.move_to_end(key)
        self.dd[key] = value
        if len(self.dd)>self.capacity:
            self.dd.popitem(last=False)
        
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)