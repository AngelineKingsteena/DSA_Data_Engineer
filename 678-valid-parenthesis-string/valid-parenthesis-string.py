class Solution:
    def checkValidString(self, s: str) -> bool:
        # https://www.youtube.com/watch?v=QhPdNS143Qg&ab_channel=NeetCode
        # quick understable in java from 7:00:- https://youtu.be/vMbNfwfPecM?feature=shared
        """ leftMin: Represents the minimum count of open parentheses 
        that still need to be closed properly to maintain the validity 
        of the string. It is used to ensure that all closing parentheses
        have a corresponding open parenthesis to match.
        leftMax: Represents the maximum count of open parentheses
        that could potentially be closed. It accounts for the
        flexibility introduced by '*' characters, which can act 
        as either open or close parentheses. """
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
            if leftMin < 0: # s = ( * ))
                leftMin = 0
        return leftMin==0 ## shows everything can be closed properly 
        
