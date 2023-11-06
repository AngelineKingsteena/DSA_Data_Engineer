class Solution:
    def checkValidString(self, s: str) -> bool:
        # https://www.youtube.com/watch?v=QhPdNS143Qg&ab_channel=NeetCode
        leftMin, leftMax = 0,0
        for c in s:
            if c =="(" :
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = ( * )
                leftMin = 0
        return leftMin==0
        