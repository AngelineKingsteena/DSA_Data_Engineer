class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode
        maxSub = nums [0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max (maxSub, curSum)
        return maxSub
                