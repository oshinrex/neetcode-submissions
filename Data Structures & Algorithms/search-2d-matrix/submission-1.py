class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m - 1

        while l <= r: 
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else: 
                m = mid
                break
            
        if l > r: 
            return False
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[m][mid]:
                r = mid - 1
            elif target > matrix[m][mid]:
                l = mid + 1
            else: 
                return True 
        return False
