import random


class RandomizedSet:
    def __init__(self):
        self.s = dict()

    def insert(self, val: int) -> bool:
        if self.s.get(val):
            return False
        else:
            self.s[val] = True
            return True

    def remove(self, val: int) -> bool:
        if self.s.get(val):
            del self.s[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        l = list(self.s.keys())
        return random.choice(l)
    
class RandomizedSet:
    def __init__(self):
        self.l = []
        self.s = dict()

    def insert(self, val: int) -> bool:
        if self.s.get(val):
            return False
        else:
            self.s[val] = True
            return True

    def remove(self, val: int) -> bool:
        if self.s.get(val):
            del self.s[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        l = list(self.s.keys())
        return random.choice(l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
