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

        oldNew = {}
        oldNew[node] = Node(node.val, None)
        q = deque()
        q.append(node)

        while q: 
            curr = q.popleft()
            for n in curr.neighbors: 
                if n not in oldNew:
                    oldNew[n] = Node(n.val, None)
                    q.append(n)
                oldNew[curr].neighbors.append(oldNew[n])

        return oldNew[node]
                