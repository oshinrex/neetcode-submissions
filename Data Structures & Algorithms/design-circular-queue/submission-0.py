class Node: 
    def __init__(self, val: int, next: Optional[Node]):
        self.val = val 
        self.next = next 

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None 
        self.last = None 
        self.k = k
        self.count = 0 

    def enQueue(self, value: int) -> bool:
       
        if not self.last:
            new_node = Node(value, None)
            new_node.next = new_node
            self.head = new_node
            self.last = new_node 
            self.count = 1
            return True
        else: 
            if self.count + 1 <= self.k:
                new_node = Node(value, self.head)
                self.last.next = new_node 
                new_node.next = self.head
                self.last = new_node
                self.count += 1
                return True 
            else:
                return False

    def deQueue(self) -> bool:
        if not self.head: 
            return False 

        if self.head == self.last:
            self.head = None
            self.last = None
            self.count -= 1
            return True
        
        new_head = self.head.next 
        self.last.next = new_head
        self.head = new_head
        self.count -= 1
        return True 

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if not self.last: 
            return -1
        
        return self.last.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()