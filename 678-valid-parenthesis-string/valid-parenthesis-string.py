class Solution:
    def checkValidString(self, s: str) -> bool:
        # https://www.youtube.com/watch?v=QhPdNS143Qg&ab_channel=NeetCode
        # quick understable in java from 7:00:- https://youtu.be/vMbNfwfPecM?feature=shared
        """ leftmax is count of open brackets that "may need to be closed"
        leftmin is count of open brackets that " need to be closed"""
        leftMin, leftMax = 0,0
        for c in s:
            if c =="(" :
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            # if max "to be closed" open bracket is -ve,string is wrong 
            ## coz it's like "atmost" u can close -ve open brackets 
            if leftMax < 0:
                return False
            # if min "to be closed" open bracket is +ve,no issues,just reset it
            # coz it's like "atleast" u can close -ve open brackets 
            if leftmin < 0: # s = ( * ))
                leftMin = 0
        return leftMin==0 ## shows everything can be closed properly 
        
