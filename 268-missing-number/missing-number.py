class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp,act=sum(range(len(nums)+1)),sum(nums)
        res=exp-act
        return res
                