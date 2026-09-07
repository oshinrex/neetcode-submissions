class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1): 
            j = i + 1

            while j < len(temperatures): 
                if temperatures[j] > temperatures[i]: 
                    res[i] = j - i
                    break
                elif res[j] == 0: 
                    break 
                else: 
                    j = res[j] + j
            
        return res