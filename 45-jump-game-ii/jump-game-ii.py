class Solution:
    def jump(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=dJ7sWiOoK7g&ab_channel=NeetCode
        res = 0
        l=r=0
        while r < len(nums) - 1: ## limit is len(nums)-1 to avoid out of bounds in later l=r+1
            farthest = 0
            for i in range(l, r + 1): # here r+1,to include r also in farthest calculation according to logic
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res +=1
        return res
        