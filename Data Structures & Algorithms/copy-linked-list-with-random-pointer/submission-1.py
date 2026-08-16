"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}

        curr = head
        while curr:
            hashmap[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        for n in hashmap: 
            next_val = n.next
            random_val = n.random 

            if next_val == None:
                hashmap[n].next = None
            else:
                hashmap[n].next = hashmap[next_val]
            
            if random_val == None:
                hashmap[n].random = None
            else:
                hashmap[n].random = hashmap[random_val]
        
        if hashmap:
            return hashmap[head]
        else:
            None
