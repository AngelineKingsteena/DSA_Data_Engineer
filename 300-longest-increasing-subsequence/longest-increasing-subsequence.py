class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## #dp[3] would be 1 because the longest sub starting from the end of the array would be 1
        dp=[1]*len(nums)
        for prev in range(len(nums)-1,-1,-1):
            for next in range(prev+1,len(nums)):
                if nums[prev]<nums[next]:
                    ## #1+dp[3] because then we have to include the last element too.
                    dp[prev]=max(dp[prev],1+dp[next])
        return max(dp)

# Create an array and initialise its all value with 1. start a loop backwards and another loop to track the value beside it. 
        # Check if it is in increasing order if it is then change the value of dp[i] to max between dp[i] or 1+dp[j]. After that return max of dp.

# lets take an example of nums = [1,2,4,3]
# dp[3] would be 1 because the longest sub starting from the end of the array would be 1. dp[2] would be 1 if nums[2]>nums[3] and because then it would not be
# increasing and dp[2] would be 1+dp[3] because then we have to include the last element too. After that dp[1] would be 1 if nums[1]>nums[2] because then again
# the sub would not be increasing and dp[1] would 1+dp[2] if we include it. After that in the case of dp[0] we will do that thing again and then our final
        #dp array would be [3,2,1,1] ([1+dp[1],1+dp[2],dp[2],dp[3]]) and our answer would be max of dp i.e 3.

# Complexity
# Time complexity:O(n^2)
# Space complexity:O(n)O(n)O(n)
