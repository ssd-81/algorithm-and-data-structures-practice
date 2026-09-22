class TimeMap:
    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        if self.hashMap[key][0][1] > timestamp:
            return ""
        
        l, r = 0, len(self.hashMap[key])-1

        while l < r:
            m = l + (r - l) // 2 + 1

            mid_cell = self.hashMap[key][m]
            if mid_cell[-1] == timestamp:
                return self.hashMap[key][m][0]
            elif mid_cell[-1] < timestamp:
                l = m 
            else:
                r = m - 1 
        return self.hashMap[key][l][0] 