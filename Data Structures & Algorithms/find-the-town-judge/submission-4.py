class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0] * n

        for rel in trust: 
            a, b = rel[0], rel[1]
            trust_score[a - 1] -= 1
            trust_score[b - 1] += 1
        
        print(trust_score)
        for i in range(len(trust_score)): 
            if trust_score[i] == n - 1:
                return i + 1

        return -1