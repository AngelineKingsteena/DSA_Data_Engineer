class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # https://www.youtube.com/watch?v=lJwbPZGo05A&ab_channel=NeetCode
        # T.C :O(n)
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        l= 0
        for r in range(len (gas)):
            ##cause gas is like profit in travelling ahead,cost is like loss and detrimental to travel
            total_gas += (gas[r] - cost[r])
            if total_gas < 0:
                total_gas=0
                ##at current total at became <0 ,so move one pointer ahead
                l=r+1
        return l


        
