class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []

        mp = {"0":"", "1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []
        path = []

        def backtrack(i): 
            if i == len(digits): 
                res.append("".join(path))
                return 

            phrase = mp.get(digits[i])
            if len(phrase) == 0: 
                backtrack(i + 1)

            for j in range(len(phrase)): 
                path.append(phrase[j])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return res