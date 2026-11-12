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
            
        node_to_new = {}
        q = deque()

        if node: 
            q.append(node)
            node_to_new[node] = Node(node.val)

        while q:
            curr = q.popleft()
            for n in curr.neighbors: 
                if n not in node_to_new:
                    new_node = Node(n.val)
                    node_to_new[n] = new_node 
                    q.append(n)

                if not node_to_new[curr].neighbors:
                    node_to_new[curr].neighbors = [node_to_new[n]]
                else:
                    node_to_new[curr].neighbors.append(node_to_new[n])

        return node_to_new[node]                 