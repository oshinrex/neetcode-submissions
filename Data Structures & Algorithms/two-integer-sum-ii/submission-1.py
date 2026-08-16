class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(numbers)):
            if target - numbers[i] in hash_map:
                return [hash_map[target - numbers[i]], i + 1]
            else: 
                hash_map[numbers[i]] = i + 1
        
        return []