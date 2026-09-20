class Node: 
    def __init__(self, val:int, prev:Optional[Node] = None, next:Optional[Node] = None):
        self.val = val 
        self.prev = prev 
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.head = None 
        self.last = None 
        self.mp = {}
    
    def move_to_front(self, curr_node: Node):
        if self.last == curr_node: 
            return
        elif curr_node == self.head: 
            self.head = self.head.next 
        else: 
            prev = curr_node.prev
            next = curr_node.next
            prev.next = next 
            next.prev = prev 

        self.last.next = curr_node
        curr_node.prev = self.last 
        self.last = curr_node 

    def get(self, key: int) -> int:
        if key in self.mp: 
            curr_node = self.mp[key]
            self.move_to_front(curr_node)
            _, val = curr_node.val
            return val

        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp: 
            curr_node = self.mp[key]
            curr_node.val = (key, value)
            self.move_to_front(curr_node)
        else: 
            if len(self.mp) == self.capacity: 
                if self.last == self.head: 
                    k, _ = self.last.val 
                    self.last = None 
                    self.head = None 
                    self.mp.pop(k)
                else: 
                    k, _ = self.head.val
                    self.head = self.head.next 
                    self.head.prev = None 
                    self.mp.pop(k)
            
            new_node = Node((key, value))
            self.mp[key] = new_node 
            
            if not self.head: 
                self.head = new_node 
                self.last = new_node 
            else: 
                self.last.next = new_node 
                new_node.prev = self.last 
                self.last = new_node 
