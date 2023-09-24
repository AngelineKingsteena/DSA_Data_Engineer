class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
            res = max(res, curMax)
        return res

# Subproblem for the DP here would be: What is the maximum and minimum product we can get for a contiguous sub-array starting from the 0th to the current element? Why do we need to maintain the minimum product while we are asked for a maximum? The fact is that elements in nums can be negative, so it possible that for some negative element the previous min possible product can turn the current product into a greater value.

# Time: O(n) - scan
# Space: O(1)
        