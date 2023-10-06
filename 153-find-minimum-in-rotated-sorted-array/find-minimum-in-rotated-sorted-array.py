class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode
        res = nums [0]
        l, r = 0, len (nums) - 1
        while l <= r:
            # if already in proper ascending order,obviously the leftmost is the minimum,so we can break out of algo,eg: in [4,5,6,7,0,1,2]
            if nums [l] < nums[r]:
                res = min(res, nums [l])
                break
            m = (l + r) // 2
            res = min(res, nums [m])
            if nums [m] >= nums [l]:
                l = m + 1
            else:
                r = m - 1
        return res
        