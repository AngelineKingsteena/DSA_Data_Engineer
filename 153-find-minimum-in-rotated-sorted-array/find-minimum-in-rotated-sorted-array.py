class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode
        res = nums [0]
        l, r = 0, len (nums) - 1
        while l <= r:
            # if already in proper ascending order,obviously the leftmost is the minimum,so we can break out of algo
            if nums [l] < nums[r]:
                res = min(res, nums [l])
                break
            m = (l + r) // 2
            ## example in [3,1,2],first iteration,l=0,r=2,nums [m]=1,end of iteration nums [m]=3
            res = min(res, nums [m])
            #  checks whether the subarray from l to m is sorted,then right might have min,cause
            # | /|      in [4,5,6,7,0,1,2] (right has the min)
            # |/ | / 
            #    |/
            if nums [l] <= nums [m]:
                l = m + 1
            # if not sorted,min might be on the other side i,.e right side
            else:
                r = m - 1
        return res
        