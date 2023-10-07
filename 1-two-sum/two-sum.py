class Solution:
   def twoSum(self, nums, target):
        seen={}
        for ind,val in enumerate(nums):
            remaining=target-val
            if remaining in seen:
                return [min(ind,nums.index(remaining)),max(ind,seen[remaining])]
            else:
                seen[val]=ind
        return []