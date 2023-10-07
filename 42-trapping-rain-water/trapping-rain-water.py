class Solution:
    ## video solution--https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len (height) - 1
        leftMax, rightMax = height [l], height[r]
        res = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height [l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        