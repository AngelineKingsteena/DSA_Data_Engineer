class Solution:
   def twoSum(self, nums, target):
    for i in range(len(nums)):
        r = target - nums[i]
        if r in nums[i+1:]:
            ind=nums[i+1:].index(r)
            return [i,ind+i+1]