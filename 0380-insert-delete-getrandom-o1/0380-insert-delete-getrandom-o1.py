import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hash_t = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_t:
            return False
    
        self.arr.append(val)

        
        self.hash_t[val] = len(self.arr)-1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hash_t:
            return False
        idx_remove_val = self.hash_t[val]
        last_val = self.arr[-1]

        self.arr[idx_remove_val] = last_val
        self.hash_t[last_val] = idx_remove_val

        self.arr.pop()
        del self.hash_t[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()