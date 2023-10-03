class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #https://leetcode.com/problems/coin-change-ii/solutions/3892702/100-dynamic-programming-video-optimal-solution/
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]
        
### The base case is set as dp[0] = 1. This is because there is one way to make up the amount of 0, which is by not using any coins (an empty combination).

#  Example 1:
# Input: amount = 5, coins = [1,2,5]

# Initialize dp as [1, 0, 0, 0, 0, 0] (size amount + 1).
## each element in dp represents an no.of ways to make index amount 
# [N for re.0,N for rs.1,N for re.2..etc]..where N=no.of ways
# For each coin denomination (1, 2, and 5):
# When considering the coin with value 1, update dp from left to right:
# dp[1] += dp[0]: dp becomes [1, 1, 0, 0, 0, 0]
# dp[2] += dp[1]: dp becomes [1, 1, 1, 0, 0, 0]
# ...
# dp[5] += dp[4]: dp becomes [1, 1, 1, 1, 1, 1]##  
# When considering the coin with value 2, update dp from left to right:
# dp[2] += dp[0]: dp becomes [1, 1, 2, 1, 1, 1]
# dp[3] += dp[1]: dp becomes [1, 1, 2, 2, 1, 1]
# ...
# dp[5] += dp[3]: dp becomes [1, 1, 2, 2, 3, 3]
# When considering the coin with value 5, update dp from left to right:
# dp[5] += dp[0]: dp becomes [1, 1, 2, 2, 3, 4]
# The final result is dp[5], which is 4. This means there are 4 different combinations to make up 5 using the coins [1, 2, 5].