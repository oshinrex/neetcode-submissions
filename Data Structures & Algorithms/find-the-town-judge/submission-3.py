class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_trust_b = defaultdict(set)
        b_trusted_by_a = defaultdict(set)

        for rel in trust: 
            a, b = rel[0], rel[1]
            a_trust_b[a].add(b)
            b_trusted_by_a[b].add(a)

        for b in b_trusted_by_a:
            if (len(b_trusted_by_a[b]) == n - 1) and (b not in a_trust_b):
                return b
        
        return -1
