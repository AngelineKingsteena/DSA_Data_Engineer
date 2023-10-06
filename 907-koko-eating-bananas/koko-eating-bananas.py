class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r= k - 1
            else:
                l = k +1
        return res
        