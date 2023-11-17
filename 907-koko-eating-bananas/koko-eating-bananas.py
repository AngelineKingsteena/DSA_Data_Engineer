class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                #time=event/ chosen speed
                hours += math.ceil(p / k)
            # similar check in https://leetcode.com/problems/time-based-key-value-store/
            if hours <= h: #(both < and ==,so no elif) bcoz problem says less or equal to is desirable
                res = min(res, k)
                r= k - 1
            else:
                ##k is denominator,so it has to be increased for  hours <= h
                l = k +1
        return res
        
