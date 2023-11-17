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
            ### cost price higher than selling price
            else:
                ## so move c.p to the place u had lesser selling price
                l =r
            ## for traversal, +=1 cause to exhaust all indice options
            r +=1
        return maxP
        
