"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []

        for i in range(len(intervals)):
            s, e = intervals[i].start, intervals[i].end
            times.append((s, 1))
            times.append((e, -1))
        
        res = 0
        curr = 0

        times.sort()

        for t in times: 
            _, to_add = t
            curr += to_add
            res = max(res, curr)
        
        return res