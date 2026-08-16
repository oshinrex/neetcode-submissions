class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0

        l, r = 0, len(people) - 1

        while l < r: 
            if people[r] + people[l] > limit: 
                r -= 1
            else:
                l += 1
                r -= 1
            res += 1
        
        return res + 1 if l == r else res