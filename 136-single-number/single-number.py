class Solution:
    def singleNumber(self, nums: List[int]) -> int:
# https://www.youtube.com/watch?v=qMPX1AOa83k&ab_channel=NeetCode
        res = 0
        for n in nums:
            ## because a(xor)a=0 ,but a(xor)0=a
            res = n ^ res
        return res
        