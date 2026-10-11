class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        max_len = sum(matchsticks) / 4
        if max(matchsticks) > max_len:
            return False 
            
        path = [0] * 4
        def backtrack(i):
            nonlocal path 
            if i == len(matchsticks):
                if path[0] == path[1] == path[2] == path[3]:
                    return True 
                else:
                    return False 
            
            for j in range(4):
                if path[j] + matchsticks[i] > max_len: 
                    continue 
                path[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True 
                path[j] -= matchsticks[i]
            
            return False

        return backtrack(0)
                