class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=1pkOgXD63yU&ab_channel=NeetCode
        l, r = 0, 1
        maxP= 0
        while r < len (prices) :
            if prices [l] < prices[r]:
                ##profit=selling price-cost price
                profit = prices[r] - prices [l]
                maxP = max (maxP, profit)
            else:
                ## move to the identified large price's index
                l =r
            r +=1
        return maxP
        
