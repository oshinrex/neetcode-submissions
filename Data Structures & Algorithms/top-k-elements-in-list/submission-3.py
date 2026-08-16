class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums))]
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n in freq: 
            buckets[freq[n] - 1].append(n)
        
        for b in range(len(buckets) - 1, -1, -1): 
            for no in buckets[b]: 
                res.append(no)
                if len(res) == k: 
                    return res
        
