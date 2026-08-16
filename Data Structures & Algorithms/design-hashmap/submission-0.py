class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.mp = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket = self.mp[key % self.size]

        for i in range(len(bucket)):
            k, _ = bucket[i]
            if k == key:
                bucket[i] = (k, value)
                return 
        
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.mp[key % self.size]

        for i, j in bucket: 
            if i == key: 
                return j
        
        return -1

    def remove(self, key: int) -> None:
        bucket = self.mp[key % self.size]

        for i in range(len(bucket)): 
            k, v = bucket[i]

            if k == key: 
                bucket.pop(i)
                break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)