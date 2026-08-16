class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the second element 
        intervals.sort(key = lambda interval: interval[1])

        ans = 0
        s, e = intervals[0]
        print(intervals)
        # if there is an overlap, remove the interval that ends later 
        for i in range(1, len(intervals)): 
            if intervals[i][0] >= e: 
                s, e = intervals[i]
            else:
                ans += 1
        return ans