class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        insert = False

        for start, end in intervals:
            # interval ends before newInterval
            if end < newInterval[0]: 
                ans.append([start, end])

            # interval starts after newInterval
            elif start > newInterval[1]: 
                if not insert:
                    ans.append(newInterval)
                    insert = True
                ans.append([start, end])

            # overlapping current array
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        if insert == False: 
            ans.append(newInterval)

        return ans