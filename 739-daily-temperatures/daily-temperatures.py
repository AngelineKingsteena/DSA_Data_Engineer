class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## video solution :-https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate (temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack. pop()
                res [stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
        