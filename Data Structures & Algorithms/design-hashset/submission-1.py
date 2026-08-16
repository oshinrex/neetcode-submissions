class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.st = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.st[key % self.size].append(key)

    def remove(self, key: int) -> None:
        bucket = self.st[key % self.size]
        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                break

    def contains(self, key: int) -> bool:
        bucket = self.st[key % self.size]
        for i in range(len(bucket)):
            if bucket[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)