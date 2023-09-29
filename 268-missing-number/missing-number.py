class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=WnPLSRLSANE&ab_channel=NeetCode
        exp,act=sum(range(len(nums)+1)),sum(nums)
        res=exp-act
        return res
                