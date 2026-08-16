class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.lst = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        ind = key % self.size
        if key not in self.lst[ind]:
            self.lst[ind].append(key)

    def remove(self, key: int) -> None:
        ind = key % self.size
        for i in range(len(self.lst[ind])): 
            if self.lst[ind][i] == key: 
                self.lst[ind].pop(i)
                break

    def contains(self, key: int) -> bool:
        ind = key % self.size
        for n in self.lst[ind]:
            if n == key: 
                return True
                break
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)