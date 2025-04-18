from random import random
class RandomizedSet:

    def __init__(self):
        self.hash={}
        self.num=[]


    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        self.hash[val] = len(self.num)
        self.num.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash: return False
        index = self.hash[val]
        lv = self.num[-1]
        self.num[index] = lv
        self.hash[lv] = index
        self.num.pop()
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        return self.num[int(random()*len(self.num))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()