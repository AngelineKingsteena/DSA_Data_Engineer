class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## video solution :- https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
        maxArea = 0
        stack = [] # pair: (index, height)
##It's for handling when the last item isn't included into the stack yet.
# Like the test case [2,4]. Without making it into a [2,4,-1], you would have to make a special case to ensure that 4 is processed, but if you added the last dummy element, then 2 and 4 will always be included in the stack and taken into account when calculating areas.
        for i, h in enumerate(heights+[-1]):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ## say in heights=[2,5]
                ## at index 1,height 5 can extend even on left side to index 0,so we pop (0,2) and use 0 as index for height 5 in stack
                maxArea = max(maxArea, height * (i - index)) #len*breadth ,where breadth is difference b/w 2 max heights' indices (current -past)
                start = index                        #   /
            ## maintains monotonically increasing stack /
            stack.append ((start, h)) 
        return maxArea
        
