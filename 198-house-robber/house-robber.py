class Solution:
    def rob(self, nums: List[int]) -> int:
        ## https://leetcode.com/problems/house-robber/solutions/1605193/with-explanation-dp-with-o-l-time-and-o-1-space-in-python/
        #edge case
        if not nums:return 0
        if len(nums) <= 2:return max(nums)
        #dp (less space)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            ## its a + nums[i] and not b + nums[i],cause alternative indices,eg:-a is at 0th index,i is at 2nd index
            a, b = b, max(a + nums[i], b)
        return b
        
