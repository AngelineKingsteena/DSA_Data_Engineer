class TimeMap:
    ## video solution :- https://www.youtube.com/watch?v=fu2cD_6E8Hw&ab_channel=NeetCode
    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store [key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get (key, [])
        # binary search
        l, r = 0, len (values) - 1
        while l <= r:
            m = (l + r) // 2
            # similar check in https://leetcode.com/problems/koko-eating-bananas/description/
            if values [m][1] <= timestamp:
                res = values [m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)