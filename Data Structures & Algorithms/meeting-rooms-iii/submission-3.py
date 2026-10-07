class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        free = [0] * n

        meetings.sort()

        for m in meetings: 
            s, e = m[0], m[1]
            min_end = free[0]
            p = 0 

            for i in range(n):
                if free[i] < min_end:
                    min_end = free[i]
                    p = i 

                if s >= free[i]:
                    break 
            
            count[p] += 1
            free[p] = max(e, free[p] + (e - s))
        
        res = count[0]
        res_i = 0 
        for i in range(n):
            if count[i] > res: 
                res = count[i]
                res_i = i 
        
        return res_i
                    