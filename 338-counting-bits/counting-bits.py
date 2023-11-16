class Solution:
    def countBits(self, n: int) -> List[int]:
        # https://www.youtube.com/watch?v=RyBM56RIWrM&ab_channel=NeetCode
        dp = [0] * (n + 1) ## n+1 cause first index is for number 0,rest are for 1 to n
        offset = 1
        for i in range(1, n + 1): ## no need 0,cause bits in 0 is 0
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
