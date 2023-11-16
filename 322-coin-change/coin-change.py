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

# idea:-
# coins = [1,2,5], amount = 5

# Initialize dp as [0, 6, 6, 6, 6, 6] (size= amount + 1).
## each element in dp represents an no.of coins required to make index amount 
# [N for re.0,N for rs.1,N for rs.2..etc]..where N=min coins required...

# For each coin denomination (1, 2, and 5):
# When considering the coin with value 1, update dp from left to right:
# dp[1]: dp becomes [0, 1, 6, 6, 6, 6]
# dp[2]: dp becomes [0, 1, 2, 6, 6, 6]
# ...
# dp[5]: dp becomes [0, 1, 2, 3, 4, 5]##min coins of 1re required
# When considering the coin with value 2, update dp from left to right:
# dp[2]: dp becomes [0, 1, 1, 3, 4, 5]
# dp[3]: dp becomes [0, 1, 1, 2, 4, 5]
# ...
# dp[5]: dp becomes [0, 1, 1, 2, 2, 3]## min no of both 1rs and 2rs coins required
# When considering the coin with value 5, update dp from left to right:
# dp[5]: dp becomes [0, 1, 1, 2, 2, 1]## min no of all 1rs,2rs,5rs coins required
# The final result is dp[5], which is 1. This means min coins requeuired to make up 5 using the coins [1, 2, 5] is 1
        
