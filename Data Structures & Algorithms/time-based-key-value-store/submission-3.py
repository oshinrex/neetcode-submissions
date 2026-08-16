class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap: 
            self.hashmap[key].append([timestamp, value])
        else: 
            self.hashmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap: 
            return ""
        
        l = 0 
        r = len(self.hashmap[key]) - 1
        mid = 0
        while l <= r: 
            mid = (l + r) // 2
            time, val = self.hashmap[key][mid]
            
            if time == timestamp: 
                return val
            elif timestamp < time: 
                r = mid - 1
            else: 
                l = mid + 1
        return "" if r < 0 else self.hashmap[key][r][1]
