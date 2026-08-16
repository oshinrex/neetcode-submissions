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
        
        hash_map = {}
        q = deque()
        q.append(node)

        while q: 
            next_node = q.popleft()
            if next_node not in hash_map:
                print(next_node.val)
                to_add = Node(next_node.val, neighbors = [])
                hash_map[next_node] = to_add

                for n in next_node.neighbors:
                    if n in hash_map: 
                        hash_map[n].neighbors.append(hash_map[next_node])
                        hash_map[next_node].neighbors.append(hash_map[n])
                    else:
                        q.append(n)
        
        return hash_map[node]




        
        
        
        

