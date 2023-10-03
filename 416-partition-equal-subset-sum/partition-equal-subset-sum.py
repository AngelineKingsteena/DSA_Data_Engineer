class Solution:
# This is a classic knapsack problem.
# Whenever you have an array, and you want to partition it based upon some criteria as shown below.
# Change the thinking from:
# "separating elements into two arrays, then calculating the difference of their sums"
# To the following:
# Whenever you partition two elements into different arrays/groups, your basically subtracting them from each other. If you put them in the same group, you're adding them. Thus, you want to try every possible combination of adding and subtracting them from eachother to see if you can reach zero!

# {num - i for i in dp} is pretty much subtracting every element in dp from the current number
# {num + i for i in dp} is pretty much adding every element in dp to the current number
# | does a union between these two sets.
    def canPartition(self, nums: List[int]) -> bool:
        #it's always possible to create an empty subset with a sum of 0.
        # Initialize a set 'possible_sums' with 0 to represent an empty subset with a sum of 0.
        possible_sums = {0}
        # Iterate through each 'num' in the input list 'nums'.
        for num in nums:
            # Create two sets:
            # 1. Subtract 'num' from each element in 'possible_sums'.
            subtracted_sums = {sum - num for sum in possible_sums}
            # 2. Add 'num' to each element in 'possible_sums'.
            added_sums = {sum + num for sum in possible_sums}
            # Combine the two sets using union (|) to update 'possible_sums' with new sums.
            possible_sums = subtracted_sums | added_sums
        # Check if 0 is in 'possible_sums', which means it's possible to partition the list into
        # two subsets with equal sums.
        return 0 in possible_sums
            