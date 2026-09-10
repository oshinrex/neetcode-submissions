class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(amt):
            curr_amt = 0
            curr = 0
            for n in nums: 
                if curr_amt + n <= amt: 
                    curr_amt += n
                    print("c: " + str(curr_amt))
                else: 
                    if curr < k - 1: 
                        curr += 1
                        curr_amt = n
                    else:
                        return False
            
            return True 

        l, r = max(nums), sum(nums)
        while l < r: 
            print(l)
            print(r)
            mid = (l + r) // 2
            if cansplit(mid):
                print("here" + str(mid))
                r = mid
            else: 
                l = mid + 1
        
        return l