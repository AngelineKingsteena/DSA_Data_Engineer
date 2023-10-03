class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #https://www.youtube.com/watch?v=H9bfqozjoqs&ab_channel=NeetCode
        # T.C:- O(amount* len(coins))
        # set default values
        dp = [amount + 1] * (amount + 1)
        dp [0] = 0 ## 0 WAYS TO MAKE AMOUNT 0
        for c in coins:
            for a in range (1, amount + 1):
            
                if a - c >= 0:## IF IT ENDS UP NEGATIVE,NO SOLUTION
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # COIN=4
                    # A=7
                    # DP[7]=1+DP[7-4]
        # return non-default values
        return dp [amount] if dp [amount] != amount + 1 else -1
        