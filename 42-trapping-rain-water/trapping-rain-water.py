class Solution:
    ## video solution--https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode
    ## idea :- min(left,right)- h[i]
    ##                  __rightMax__
    ## __leftMax__     |
    ##            |~~~~|
    ##            |h[i]|
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len (height) - 1
        leftMax, rightMax = height [l], height[r]
        count = 0
        while l < r:
            if leftMax <= rightMax:
                # first step is to move ,cause no water can be held at left extreme 
                l += 1
                # to avoid negative at index 0 in eg [0,1,0,2]
                # no issues if the below 2 lines is returning 0,incase of same value subtraction
                # cause we intended to make any -ve as zero anyway,so anyway we're going to disregard values
                leftMax = max(leftMax, height[l])
                count += leftMax - height [l] # at index 0 in eg [0,1,0,2], it'll be 1-1=0
            else:
                # first step is to move ,cause no water can be held at right extreme
                r -= 1
                rightMax = max(rightMax, height[r])
                count += rightMax - height[r]
        return count
        
