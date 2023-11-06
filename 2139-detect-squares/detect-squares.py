class DetectSquares:
# https://www.youtube.com/watch?v=bahebearrDc&ab_channel=NeetCode
    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        #print('New')
        for x, y in self.pts:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            if (px, y) in self.pts and (x, py) in self.pts:
                # Multiply with the number of occurrences of the repeated point represented by self.pts[(x, y)]
                res += self.pts[(px, y)] * self.pts[(x, py)] * self.pts[(x, y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
