class Solution:
    def canJump(self, nums: List[int]) -> bool:
# https://www.youtube.com/watch?v=Yan0cv2cLy8&ab_channel=NeetCode
        goal = len(nums) - 1
        for i in range(len (nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                ## move goal inwards(towards left) to the index which helped reach prior(farther right) goal
                goal = i
        return goal == 0
        
