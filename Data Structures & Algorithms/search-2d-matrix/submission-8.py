class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1, r2 = 0, len(matrix) - 1
        
        # find correct row
        while r1 <= r2:
            mid = (r1 + r2) // 2
            if matrix[mid][0] > target:
                if (mid - 1) < 0: 
                    return False
                r2 = mid - 1
            elif matrix[mid][len(matrix[mid]) - 1] < target: 
                if (mid + 1) >= len(matrix):
                    return False
                r1 = mid + 1
            else:
                r1 = mid
                break 
        
        print(r1)
        c1, c2 = 0, len(matrix[0]) - 1

        while c1 <= c2: 
            mid = (c1 + c2) // 2
            print(mid)
            if matrix[r1][mid] == target: 
                return True 
            elif matrix[r1][mid] > target:
                c2 = mid - 1
            else:
                c1 = mid + 1
        
        return False