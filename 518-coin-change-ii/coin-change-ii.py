class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://www.youtube.com/watch?v=Mjy4hd2xgrs&ab_channel=NeetCode
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        
        return dp[amount]
        