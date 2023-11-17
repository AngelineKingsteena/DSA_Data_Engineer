class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        ### in exampple [10,15,20]
        # [10,15,20,0]
        # [min(25,30),min(35,15),20,0]#0 coz u pay nothing to keep staying on top;
        # 20 coz u have only one option pay 20,do one jump,whereas rest of the steps have option of one jump or 2 jumps
        cost=c.copy()
        cost.append(0)
        for i in range(len (cost) - 3, -1, -1):
            #### min(15+20,15+0)
            cost[i] += min (cost[i + 1], cost[i + 2])
        return min(cost [0], cost [1]) #because question says:-You can either start from
        #the step with index 0, or the step with index 1.
        ## so the answer is 15
