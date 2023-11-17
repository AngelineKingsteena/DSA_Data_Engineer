class Solution:
    def jump(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=dJ7sWiOoK7g&ab_channel=NeetCode
        jumps, current_end, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                current_end = farthest
                jumps += 1

        return jumps
        
