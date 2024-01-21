class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode
        ### 1.max and  min spped at which u can eat these piles
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            ## 2. assumptive speed
            k = (l + r) // 2
            ### 3. hours that it would take to finish eating full pile wid above assumptive speed
            hours = 0
            for p in piles:
                #time=event/ chosen speed
                hours += math.ceil(p / k)
            # similar check in https://leetcode.com/problems/time-based-key-value-store/
            ### 4. can the hour be made <= target hour, if so adjust the range of speed
            if hours <= h: #(both < and ==,so no elif) bcoz problem says less or equal to is desirable
                res = min(res, k)
                r= k - 1
            else:
                ##k is denominator,so it has to be increased for  hours <= h
                l = k +1
        return res
        
