class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## explanation https://youtu.be/bNvIQI2wAjk?feature=shared
        ## T.C= O(n)
        res = [1] * (len (nums))
        prefix = 1
        for i in range(len (nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len (nums) - 1, -1, -1):
            res[i]*= postfix
            postfix *= nums[i]
        return res
        