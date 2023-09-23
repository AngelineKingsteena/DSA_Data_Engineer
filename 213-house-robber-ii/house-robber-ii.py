class Solution:
    def rob(self, nums: List[int]) -> int:
        ##nums[0] for case like nums =[1]
        return max(nums[0],self.helper(nums[:-1]),self.helper(nums[1:]))

    def helper(self,nums: List[int]) -> int:
        ## https://leetcode.com/problems/house-robber/solutions/1605193/with-explanation-dp-with-o-l-time-and-o-1-space-in-python/
        #edge case
        if not nums:return 0
        if len(nums) <= 2:return max(nums)
        #dp (less space)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            a, b = b, max(a + nums[i], b)
        return b
        