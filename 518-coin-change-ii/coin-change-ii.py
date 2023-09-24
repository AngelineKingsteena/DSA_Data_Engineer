class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #https://leetcode.com/problems/coin-change-ii/solutions/3892702/100-dynamic-programming-video-optimal-solution/
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        
        return dp[amount]
        