class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=WnPLSRLSANE&ab_channel=NeetCode
        res = len(nums)
        for i in range(len (nums)):
            res += (i - nums [i])
        return res
                