"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [0] * len(intervals)
        end = [0] * len(intervals)

        for i in range(len(intervals)): 
            start[i] = intervals[i].start
            end[i] = intervals[i].end
        
        start.sort()
        end.sort() 

        sp = 0
        ep = 0
        max_count = 0
        curr = 0

        while sp < len(start) or ep < len(end): 
            if sp < len(start) and ep < len(end):
                if start[sp] < end[ep]:
                    curr += 1
                    max_count = max(max_count, curr)
                    sp += 1
                elif start[sp] == end[ep]:
                    sp += 1
                    ep += 1
                else: 
                    curr -= 1
                    ep += 1
            else: 
                break 
        
        return max_count