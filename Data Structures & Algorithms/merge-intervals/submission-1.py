class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        s, e = intervals[0]

        for i in range(1, len(intervals)):
            if e < intervals[i][0]: 
                ans.append([s, e])
                s, e = intervals[i]

            else: 
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
        
        ans.append([s, e])
        
        return ans