class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1
        res = [0] * (len(matrix) * len(matrix[0]))

        curr = 0

        while curr < len(res): 
            for i in range(l, r+1): 
                res[curr] = matrix[top][i]
                curr += 1
            
            top += 1
            if top > bot: 
                break
            
            for i in range(top, bot+1): 
                res[curr] = matrix[i][r]
                curr += 1

            r -= 1
            if l > r: 
                break
            
            for i in range(r, l - 1, -1): 
                res[curr] = matrix[bot][i]
                curr += 1
            
            bot -= 1
            if top > bot: 
                break
            
            for i in range(bot, top - 1, -1): 
                res[curr] = matrix[i][l]
                curr += 1
            
            l += 1
            if l > r: 
                break
        
        return res
