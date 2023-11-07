class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# https://www.youtube.com/watch?v=I7j0F7AHpb8&ab_channel=NeetCode
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -› i + 2 coz after selling there's a compulsory cooldown
        dp = {} # key=(i, buying) val=max_profit
        def dfs(i, buying) :
            if i >= len (prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]#buying is only available 
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]#not buying,coz you can only either sell or cool down
                dp[ (i, buying)] = max (buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices [i]#not buying,coz you can cool down
                dp[(i, buying)] = max (sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)
                
