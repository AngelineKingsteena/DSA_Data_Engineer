class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
# https://www.youtube.com/watch?v=g0npyaQtAQM&ab_channel=NeetCode
        dp = {} # (index, total) -› # of ways
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            ### important memoisation if block
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i])+
            backtrack(i + 1, total - nums[i]))
            return dp[ (i, total)]
        return backtrack(0, 0)

# With memoization:
# To avoid recalculating the same subproblems, we use the dp dictionary to store the results for specific combinations of (i, total) that we have already computed. If we encounter the same combination again, we simply look up the result in the dictionary instead of recomputing it.

# For example, when we reach (i=2, total=3) for the first time, we calculate backtrack(3, 6) and backtrack(3, 0) and store these results in the dp dictionary with the corresponding key (2, 3) as shown below:

# dp[(2, 3)] = 2  # The number of ways to reach 3 with remaining elements.
# Now, when we encounter (i=2, total=3) again during subsequent recursive calls, we check the dp dictionary. Since (2, 3) is already in the dictionary, we simply return the precomputed value 2. This avoids redundant calculations and significantly reduces the time complexity of the algorithm.





        