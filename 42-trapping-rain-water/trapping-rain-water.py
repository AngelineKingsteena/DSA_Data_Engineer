class Solution:
    ## video solution--https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode
    ## idea :- min(left,right)- h[i]
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len (height) - 1
        leftMax, rightMax = height [l], height[r]
        count = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                # to avoid negative at index 0 in eg [0,1,0,2]
                leftMax = max(leftMax, height[l])
                count += leftMax - height [l] # at index 0 in eg [0,1,0,2], it'll be 1-1=0
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                count += rightMax - height[r]
        return count
        
