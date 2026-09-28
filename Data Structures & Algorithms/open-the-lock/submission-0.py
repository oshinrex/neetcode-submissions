class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: 
            return -1
        
        q = deque()
        q.append(("0000", 0))

        visited = set() 
        visited.add("0000")

        while q: 
            lock, steps = q.popleft() 

            if lock == target: 
                return steps

            for i in range(4):
                forward = int(lock[i]) + 1
                backward = int(lock[i]) - 1
                if forward > 9: 
                    forward = 0 
                
                if backward < 0: 
                    backward = 9 
                
                lock1 = lock[:i] + str(forward) + lock[i + 1:]
                lock2 = lock[:i] + str(backward) + lock[i + 1:]

                if lock1 not in visited and lock1 not in deadends: 
                    q.append((lock1, steps + 1))
                    visited.add(lock1)
                
                if lock2 not in visited and lock2 not in deadends:
                    q.append((lock2, steps + 1))
                    visited.add(lock2)
        
        return -1
            
