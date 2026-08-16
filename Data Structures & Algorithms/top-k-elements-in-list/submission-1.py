class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        res = [[] for _ in range(len(nums) + 1)]

        for c in count: 
            res[count[c]].append(c)
        
        ret = [0] * k
        p = 0

        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res[i])):
                if p < len(ret):
                    ret[p] = res[i][j]
                    p += 1
        
        return ret
