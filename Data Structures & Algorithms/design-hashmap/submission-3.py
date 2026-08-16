class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.mp = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket = key % self.size
        for i, pair in enumerate(self.mp[bucket]):
            k, v = pair
            if k == key:
                self.mp[bucket][i] = (k, value)
                return
        self.mp[bucket].append((key, value))

    def get(self, key: int) -> int:
        bucket = key % self.size
        for k, v in self.mp[bucket]:
            if k == key: 
                return v
        
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.size
        for i, pair in enumerate(self.mp[bucket]):
            k, _ = pair
            if k == key: 
                self.mp[bucket].pop(i)
                break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)