class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = [0] * (len(left) + len(right))
            l, r = 0, 0
            p = 0

            while l < len(left) or r < len(right):
                if l == len(left):
                    while r < len(right):
                        res[p] = right[r]
                        p += 1
                        r += 1
                elif r == len(right):
                    while l < len(left):
                        res[p] = left[l]
                        p += 1
                        l += 1
                elif left[l] <= right[r]:
                    res[p] = left[l]
                    l += 1
                    p += 1
                else: 
                    res[p] = right[r]
                    r += 1
                    p += 1
            
            return res

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        return merge_sort(nums)