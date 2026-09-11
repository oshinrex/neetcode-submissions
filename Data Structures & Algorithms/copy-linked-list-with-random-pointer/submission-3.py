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
        # links old node to new node
        mp = {}
        curr = head
        prev = None 
        while curr: 
            if curr not in mp: 
                mp[curr] = Node(curr.val, None, None)

            if curr.next and curr.next not in mp: 
                mp[curr.next] = Node(curr.next.val)
            
            if curr.next:
                mp[curr].next = mp[curr.next]

            if curr.random and curr.random not in mp: 
                mp[curr.random] = Node(curr.random.val)
            
            if curr.random:
                mp[curr].random = mp[curr.random]

            curr = curr.next
        
        return mp[head] if head else None