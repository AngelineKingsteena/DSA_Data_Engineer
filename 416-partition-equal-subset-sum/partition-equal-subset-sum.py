class Solution:
# This is a classic knapsack problem.
# Whenever you have an array, and you pretty much want to partition it based upon some criteria, you can use a similar format as shown below.
# Change the thinking from:
# "separating elements into two arrays, then calculating the difference of their sums"
# To the following:
# Whenever you partition two elements into different arrays/groups, your basically subtracting them from each other. If you put them in the same group, you're adding them. Thus, you want to try every possible combination of adding and subtracting them from eachother to see if you can reach zero!
# {num - i for i in dp} is pretty much subtracting every element in dp from the current number
# {num + i for i in dp} is pretty much adding every element in dp to the current number
# | does a union between these two sets.
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        for num in nums:
            dp = {num - i for i in dp} | {num + i for i in dp} 
        return 0 in dp
        