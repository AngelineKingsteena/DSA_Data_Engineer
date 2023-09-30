class Solution(object):
    def isHappy(self, n):
        hset = set()
        while n != 1:
            ## TO AVOID CCYCLE --> 2 will eventaully become 37 and then 61-->it'll again become 37
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True