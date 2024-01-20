class Solution:
    def climbStairs(self, n: int) -> int:
        # # video solution :- https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode
        # # s.c :-
        # # t.c :-n
        # # [newOne,newTwo/oldOne,oldTwo]
        # # [1+1,1,1]
        # one, two = 1, 1 #two is no. of ways to reach top from top
        #  #one is no. of ways to reach top from top before step
        # ## skip last two
        # for i in range(n - 1):
        #     # temp = one
        #     # one = one + two
        #     # two = temp
        #     one,two=one + two,one
        # return one
        # Edge cases
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp=[0]*(n-2) +[2,1]
        print(dp)

        for i in range(n-3,-1,-1):
            dp[i]=dp[i+1]+dp[i+2]
        return dp[0]
        
