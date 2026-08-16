class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 = 0
        r2 = len(matrix) - 1
        mid = 0
        while r1 <= r2: 
            mid = (r1 + r2) // 2 
            if target == matrix[mid][0] or target == matrix[mid][-1]:
                return True
            elif target > matrix[mid][0] and target < matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                r2 = mid - 1
            else:
                r1 = mid + 1
        
        l1, l2 = 0, len(matrix[0]) - 1
        while l1 <= l2:
            m = (l1 + l2) // 2
            if target == matrix[mid][m]: 
                return True
            elif target < matrix[mid][m]:
                l2 = m - 1
            else: 
                l1 = m + 1
        
        return False



