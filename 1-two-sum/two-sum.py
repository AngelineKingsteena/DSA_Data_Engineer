class Solution:
   def twoSum(self, nums, target):
        seen={}
        for i,val in enumerate(nums):
            remaining=target-val
            if remaining in seen:
                return [min(i,nums.index(remaining)),max(i,seen[remaining])]
            else:
                seen[val]=i
        return []