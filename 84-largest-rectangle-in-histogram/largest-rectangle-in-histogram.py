class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## video solution :- https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
        maxArea = 0
        stack = [] # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append ((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len (heights) - i))
        return maxArea
        