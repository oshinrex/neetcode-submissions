"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        
        mp = {}

        stack = [node]
        new_node = Node(node.val, [])
        mp[node] = new_node 

        while stack: 
            curr = stack.pop()
            
            connected = curr.neighbors

            for n in connected:
                if n in mp: 
                    mp[curr].neighbors.append(mp[n])
                else: 
                    new_node = Node(n.val, [])
                    mp[n] = new_node 
                    mp[curr].neighbors.append(new_node)

                    stack.append(n)

        return mp[node]
