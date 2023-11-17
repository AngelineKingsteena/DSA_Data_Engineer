class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# https://www.youtube.com/watch?v=I7j0F7AHpb8&ab_channel=NeetCode
        # State: Buying or Selling?
        cache = {} # key=(i, buying) val=max_profit
        def dp(i, buying) :
            if i >= len (prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]#buying is only available 
            cooldown = dp(i + 1, buying)
            if buying:
                # If Buy -> i + 1
                buy = dp(i + 1, not buying) - prices[i]#not buying,coz you can only either sell or cool down
                cache[ (i, buying)] = max (buy, cooldown)
            else:
                # If Sell -› i + 2 coz after selling there's a compulsory cooldown
                sell = dp(i + 2, not buying) + prices [i]#not buying,coz you can cool down
                cache[(i, buying)] = max (sell, cooldown)
            return cache[(i, buying)]
        return dp(0, True)
                
